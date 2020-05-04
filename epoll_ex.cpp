#include<cstdio>
#include<iostream>
#include<string.h>
#include<fcntl.h>

using namespace std;

#include<sys/unistd.h>
#include<sys/socket.h>
#include<sys/epoll.h>
#include<arpa/inet.h>

#define LISTEN_BACKLOG 15

int main(int argc, char* argv[]){
    
    int error_check;
    int server_fd = socket(PF_INET, SOCK_STREAM, 0);
    if(server_fd < 0){
        printf("socket() error\n");
        return 0;
    }

    int flags = fcntl(server_fd, F_GETFL);
    flags |= O_NONBLOCK;

    if(fcntl(server_fd, F_SETFL, flags) < 0){
        printf("server_fd fcntl() error\n");
        return 0;
    }

    int option = true;
    error_check = setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(option));

    if(error_check < 0){
        printf("setsockopt() error[%d]\n", error_check);
        close(server_fd);
        return 0;
    }

    if(listen(server_fd, LISTEN_BACKLOG) < 0){
        printf("listen() error\n");
        close(server_fd);
        return 0;
    }

    int epoll_fd = epoll_create(1024);
    if(epoll_fd < 0){
        printf("epoll_create() error\n");
        close(server_fd);
        return 0;
    }

    struct epoll_event events;
    events.events = EPOLLIN | EPOLLET;
    events.data.fd = server_fd;

    if(epoll_ctl(epoll_fd, EPOLL_CTL_ADD, server_fd, &events) < 0){
        printf("epoll_ctl() error\n");
        close(server_fd);
        close(epoll_fd);
        return 0;
    }

    int MAX_EVENTS = 1024;
    struct epoll_event epoll_events[MAX_EVENTS];
    int event_count;
    int timeout = 1;

    while(true){
        event_count = epoll_wait(epoll_fd, epoll_events, MAX_EVENTS, timeout);
        if(event_count < 0){
            printf("epoll_wait() error\n");
            return 0;
        }

        for(int i = 0; i < event_count ; i++){
            if(epoll_events[i].data.fd == server_fd){
                int client_fd;
                int client_len;
                struct sockaddr_in client_addr;

                printf("User Accept\n");
                client_len = sizeof(client_addr);
                client_fd = accept(server_fd, (struct sockaddr*)&client_addr, (socklen_t*)&client_len);
                int flags = fcntl(client_fd, F_GETFL);
                flags |= O_NONBLOCK;

                if(fcntl(client_fd, F_SETFL, flags) < 0){
                    printf("client_fd[%d] fcntl() error\n", client_fd);
                    return 0;
                }

                if(client_fd < 0){
                    printf("accept() error\n");
                    return 0;
                }

                struct epoll_event events;
                events.events = EPOLLIN | EPOLLET;
                events.data.fd = client_fd;

                if(epoll_ctl(epoll_fd, EPOLL_CTL_ADD, client_fd, &events) < 0){
                    printf("client epoll_ctl() error\n");
                    close(client_fd);
                    continue;
                }
            }
            else{
                int str_len;
                int client_fd = epoll_events[i].data.fd;
                char data[4096];
                str_len = read(client_fd, &data, sizeof(data));
                if (str_len == 0)
                {
                    // 클라이언트 접속 종료 요청
                    printf("Client Disconnect [%d]\n", client_fd);
                    close(client_fd);
                    epoll_ctl(epoll_fd, EPOLL_CTL_DEL, client_fd, NULL);
                }
                else
                {
                    // 접속 종료 요청이 아닌 경우 요청의 내용에 따라 처리.
                    printf("Recv Data from [%d]\n", client_fd);
                }
            }
        }
    }


}

