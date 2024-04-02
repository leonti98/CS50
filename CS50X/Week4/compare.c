#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("s: ");

    printf("%p\n", s);
    printf("%p\n", t);
    // if (strcmp(s, t) == 0)
    // {
    //     printf("Same\n");
    // }
    // else
    // {
    //     printf("Different\n");
    // }
}
