#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int amount;
    do
    {
        amount = get_int("Height: ");
    }
    while (amount < 1 || amount > 8);

    for (int height = 1; height < amount + 1; height++)
    {
        int distance = amount - height;
        for (int space = distance; space > 0; space--)
        {
            printf(" ");
        }

        for (int c = 0; c < height; c++)
        {
            printf("#");
        }
        printf("  ");
        for (int width = 0; width < height; width++)
        {
            printf("#");
        }

        printf("\n");
    }
}
