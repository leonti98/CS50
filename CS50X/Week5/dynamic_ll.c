#include <stdio.h>
#include <stdlib.h>

struct node
{
    int num;
    struct node *ptr;
};

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
        struct node *lnode_link = malloc(sizeof(struct node));
        end_node->ptr = lnode_link;
        lnode_link->num = atoi(argv[i]);
        // printf("lnode_link->num %i\n", lnode_link->num);
        // printf("end_node->ptr %p\n", end_node->ptr);
        lnode_link->ptr = NULL;
        end_node = lnode_link;
        // printf("lnode_link->num %i\n", lnode_link->num);
        // printf("lnode_link->ptr %p\n", lnode_link->ptr);
        // printf("end_node->ptr %p\n", end_node->ptr);
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
