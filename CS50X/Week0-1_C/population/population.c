#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int current_size = start_size;
    while (current_size < end_size)
    {
        current_size += (current_size / 3) - (current_size / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
