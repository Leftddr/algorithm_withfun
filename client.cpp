#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#include<sys/types.h>

#define BUF_SIZE 1024

int main(int argc, char* argv[]){
    struct sockaddr_in client_addr;
    char *ip = argv[1];
    in_port_t port = atoi(argv[2]);
    char chat_data[BUF_SIZE];

    if(argc != 3){
        printf("Usage : ./filename [ip] [port] \n");
        exit(0);
    }

    int client_fd = socket(PF_INET, SOCK_STREAM, 0);

    client_addr.sin_addr.s_addr = inet_addr(ip);
    client_addr.sin_family = AF_INET;
    clinet_addr.sin_port = htons(port);

    if(connect(client_fd, (struct sockaddr*)&client_addr, sizeof(client_addr)) == -1){
        printf("connect() error\n");
        close(client_fd);
        return 0;
    }

    while(1){
        fgets(chat_data, sizeof(chat_data), stdin);
        send(client_fd, chat_data, sizeof(chat_data), 0);
    }

    close(client_fd);
}