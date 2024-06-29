#include <stdio.h>
#include <stdlib.h>


typedef struct node
{
    int number;
    struct node *next;
}
node;


int main(int argc, char *argv[])
{
    // exaple 3. Linke list
    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
        int number = atoi(argv[i]);

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        n->number = number;
        n->next = NULL;

        n->next = list;
        list = n;
    }

    node *ptr = list;
    while (ptr != NULL)
    {
        printf("%i\n", ptr->number);
        ptr = ptr->next;
    }

    // for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    ptr = list;
    while ( ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }


    // // example 2
    // int *list = malloc(3 * sizeof(int));
    // if (list == NULL)
    // {
    //     return 1;
    // }
    // list[0] = 1;
    // list[1] = 2;
    // list[2] = 3;

    // // ...

    // int *tmp = realloc(list, 4 * sizeof(int));
    // if (tmp == NULL)
    // {
    //     free(list);
    //     return 1;
    // }
    // list = tmp;

    // for (int i = 0; i < 4; i++)
    // {
    //     printf("%i\n", list[i]);
    // }

    // free(list);

    // first example!!!!!!!

    // int list[3];

    // list[0] = 1;
    // list[1] = 2;
    // list[2] = 3;

    // for (int i = 0; i < 3; i++)
    // {
    //     printf("%i\n", list[i]);
    // }

    return 0;
}
