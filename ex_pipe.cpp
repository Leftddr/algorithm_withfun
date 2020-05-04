#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 255

int main(int argc, char* argv[]){

    int fd[2];
    char buf[BUF_SIZE];
    pid_t pid;

    if(pipe(fd) < 0){
        perror("pipe error : ");
        exit(0);
    }

    if((pid = fork()) < 0){
        perror("fork() error : ");
        exit(0);
    }

    else if(pid == 0){
        close(fd[0]);
        while(1){
            memset(buf, 0x00, BUF_SIZE);
            sprintf(buf, "Hello : %d\n", getpid());
            write(fd[1], buf, strlen(buf));
            sleep(1);
        }
    }

    else{
        close(fd[1]);
        int n;
        while(1){
            memset(buf, 0x00, BUF_SIZE);
            n = read(fd[0], buf, BUF_SIZE);
            fprintf(stderr, "%s", buf);
        }
    }
}

