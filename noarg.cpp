#include <stdio.h>
#include <stdarg.h>

void printNumbers(const char*, ...);

int main(int argc, char* argv[]){
    printNumbers("%d + %d = %d\n", 10, 20, 10 + 20);
}

void printNumbers(const char* fmt, ...){
    char buf[128] = {0,};
    va_list ap;
    va_start(ap, fmt);
    vsprintf(buf, fmt, ap);
    printf("%s", buf);
    va_end(ap);
}