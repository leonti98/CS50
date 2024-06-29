#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    int length = 0;
    char last_char;
    int number = 0;
    int digit = 0;
    int multiplier = 1;
    while (length != 1)
    {
        length = strlen(input);
        printf("Length = %i\n", length);
        // get last char using index
        last_char = input[length - 1];
        printf("Last_char = %c\n", last_char);
        // conver to int
        digit = last_char - '0';
        printf("digit = %i\n", digit);
        // add all digits to right place
        number += digit * multiplier;
        printf("number = %i\n", number);
        // multiply multiplier by 10**n to get right number
        multiplier *= 10;
        input[length - 1] = '\0';
    }
    return number;
}
