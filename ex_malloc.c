#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <malloc.h>

typedef struct Node{
    int data;
    struct Node* next;
    struct Node* prev;
}node;

typedef struct List{
    int len;
    struct Node* head;
    struct Node* tail;
}list;

list* manager;
node* first;

void init();
void add(int);
void delete(int);

int main(int argc, char* argv[]){
    init();
    printf("%d\n", manager->head->data);
    for(int i = 1 ; i < 10 ; i++)
        add(i);
    delete(2);
}

void init(){

    manager = (list*)malloc(sizeof(list));
    first = (node*)malloc(sizeof(node));

    manager->len = 1;
    manager->head = first;
    manager->tail = first;

    first->data = 0;
    first->next = NULL;
    first->prev = NULL;
}

void add(int num){
    node* temp = (node*)malloc(sizeof(node));
    temp->data = num;

    manager->head->prev = temp;
    manager->tail->next = temp;
    temp->prev = manager->tail;
    temp->next = manager->head;

    manager->tail = temp;
    manager->len++;
}

void delete(int index){
    if(manager->len < index){
        printf("no index"); 
        return;
    }
    node* temp = manager->head;
    for(int i = 1 ; i < index ; i++){
        temp = temp->next;
    }
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    manager->len--;
}