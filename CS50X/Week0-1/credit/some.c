#include <stdio.h>

int main()
{
    long num = 400360;
    int sum = 0;
    while (num != 0)
    {
        num = num / 10;
        int digit = num % 10;
        num = num / 10;
        printf("%d ", digit);
        printf("%li ", num);
        sum += digit;
    }
}

