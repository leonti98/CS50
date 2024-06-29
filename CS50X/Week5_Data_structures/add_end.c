#include <stdio.h>
#include <stdlib.h>

struct node
{
    int num;
    struct node *ptr;
};

struct node *add_end(struct node *end_node, int data);

int main(int argc, char *argv[])
{
    struct node *ll = malloc(sizeof(struct node));
    if (ll == NULL)
    {
        printf("could not allocate");
        return 1;
    }
    ll->num = 0;
    ll->ptr = NULL;

    // struct node *ll_start = ll;
    // printf("ll = %p\n", ll);

    struct node *end_node = malloc(sizeof(struct node));
    if (end_node == NULL)
    {
        printf("could not allocate");
        return 1;
    }
    end_node = ll;
    // printf("end_node = %p\n", end_node);

    for (int i = 1; i < argc; i++)
    {
        //add_end function returns link to added node
        end_node = add_end(end_node, atoi(argv[i]));
    }

    struct node *traverser = malloc(sizeof(struct node));
    if (traverser == NULL)
    {
        printf("could not allocate");
        return 1;
    }

    int count = 0;
    traverser = ll;
    while (traverser != NULL)
    {
        count++;
        printf("data: %i\n", traverser->num);
        traverser = traverser->ptr;
    }
    printf("count: %i\n", count);
}

// function to add node at the end of the linked list
struct node *add_end(struct node *end_node, int data)
//struct node * is just data type
{
    struct node *temp = malloc(sizeof(struct node));
    temp->num = data;
    temp->ptr = NULL;

    end_node->ptr = temp;
    return temp;
}
