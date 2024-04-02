#include <stdio.h>
#include <cs50.h>
int main()
{
    long num = get_long("Number: ");
    // Save last figit of number
    int tot = num % 10;
    // Used to ge every second from first.
    long num_for_firsts = num/10;
    // Used in llop to get first digit
    long first_digit = num;
    // printf("first digit: %li\n", first_digit);
    int sum = 0;

    // Loop to get every second number starting from second digit.
    while(num != 0)
    {
        num = num / 10;
        int digit = num % 10;
        num = num / 10;
        int multy = digit * 2;
        // Loop to get digits if after multiplication exceeded 10.
        while(multy != 0)
        {
            int one = multy % 10;
            multy = multy / 10;
            sum += one;
        }
    }

    // printf("\nsum: %i\n", sum);
    // printf("done with seconds\n");

    // Loop to get every second digit statrting from first digit.
    while(num_for_firsts != 0)
    {
        num_for_firsts = num_for_firsts / 10;
        int first = num_for_firsts % 10;
        // printf("%d ", first);
        num_for_firsts = num_for_firsts / 10;

        tot += first;
    }

    // printf("\ntot: %i\n", tot);
    sum += tot;
    // printf("sum = %i\n", sum);

    // secont digit off summuary to check validity.
    int second_of_sum = sum%10;
    int digit;

    // Loop which gets only first digit of number to recognize card issuer.
    while(first_digit != 0)
    {
        int dig = first_digit % 10;
        first_digit = first_digit / 10;
        digit = dig;
    }

    // printf("digit = %i\n", digit);
    if(digit == 3 && second_of_sum ==0)
    {
        printf("AMEX\n");
    }
    else if(digit == 5 && second_of_sum ==0)
    {
        printf("MASTERCARD\n");
    }
    else if(digit == 4 && second_of_sum ==0)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
