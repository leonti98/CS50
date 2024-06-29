#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};

int main() {
    // create ponter to head/root to access first node and every consequent node
    struct node *head = malloc(sizeof(struct node));
    printf("struct node *head = malloc(sizeof(struct node))\n");
    printf("head->data %d\n", head->data);
    printf("head->link %p\n\n", head->link);

    head->data = 45;
    head->link = NULL;
    printf("head->data = 45;\nhead->link = NULL; \n");
    printf("head->data %d\nhead->link %p\n\n",head->data, head->link );
    // create pointer to last node to append new nodes
    struct node *current = malloc(sizeof(struct node));
    printf("struct node *current = malloc(sizeof(struct node)\n");
    printf("current->data %d\nhead->data %d\n", current->data, head->data);
    printf("head->link %p\ncurrent->link %p\n\n",head->link, current->link);
    current->data = 98;
    current->link = NULL;
    printf("current->data = 98;\ncurrent->link = NULL;\n");
    printf("current->data %d\nhead->data %d\n", current->data, head->data);
    printf("head->link %p\n", head->link);
    printf("current->link %p\n\n", current->link);
    head->link = current;
    printf("head->link = current;\n");
    printf("head->link %p\ncurrent->link %p\n", head->link, current->link);
    current = malloc(sizeof(struct node));
    printf("current->link %p\n", current->link);
    current->data = 3;
    current->link = NULL;
    head->link->link = current;
    printf("current->data %d\nhead->data %d\n", current->data, head->data);
    printf("current: %p\n", current);
    printf("current->link %p\n\n", current->link);

    // count nodes and loop through nodes
    struct node *loopnode = malloc(sizeof(struct node));
    int counter = 0;
    loopnode->link = head->link;
    loopnode->data = head->data;
    while(loopnode != NULL)
    {
        printf("loopnode data: %i\n", loopnode->data);
        printf("loopnode link: %p\nnode end\n\n", loopnode->link);
        loopnode = loopnode->link;
        counter++;
    }
    printf("counter: %i\n", counter);

    // only node count
    int count = 0;
    struct node *ptr = NULL;
    ptr = head;
    while(ptr != NULL)
    {
        count++;
        ptr = ptr->link;
    }
    printf("count %i\n", count);




    // struct node *current2 = malloc(sizeof(struct node));
    // current2->data = 3;
    // current2->link = NULL;
    // current->link = current2;
    // printf("current: %p\n", current);
    // printf("current->link %p\n", current->link);
    return 0;
}
