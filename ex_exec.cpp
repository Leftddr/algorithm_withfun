#include<bits/stdc++.h>
#include<unistd.h>
#include<stdlib.h>
using namespace std;

int main(int argc, char* argv[]){
    char *data1[] = {"ls", "-a", 0};
    char *data2[] = {"a", "b", 0};

    execl("/bin/ls", "ls", "-a", 0);

    return 0;
}