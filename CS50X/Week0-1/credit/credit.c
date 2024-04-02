#include <cs50.h>
#include <stdio.h>
int main()
{
    long num;
    int counter = 0;
    counter = 0;
    num = get_long("Number: ");
    long holder = num;
    // Counter to not accept too long or too short numbers
    while (holder > 0)
    {
        holder /= 10;
        counter++;
    }

    if (counter < 13 || counter > 17)
    {
        printf("INVALID\n");
    }
    else
    {
        // Save last figit of number
        int tot = num % 10;
        // Used to ge every second from first.
        long num_for_firsts = num / 10;
        // Used in llop to get first digit
        long first_digits = num;
        int sum = 0;

        // Loop to get every second number starting from second digit.
        while (num != 0)
        {
            num = num / 10;
            int digit = num % 10;
            num = num / 10;
            int multy = digit * 2;
            // Loop to get digits if after multiplication exceeded 10.
            while (multy != 0)
            {
                int one = multy % 10;
                multy = multy / 10;
                sum += one;
            }
        }

        // Loop to get every second digit statrting from first digit.
        while (num_for_firsts != 0)
        {
            num_for_firsts = num_for_firsts / 10;
            int first = num_for_firsts % 10;
            num_for_firsts = num_for_firsts / 10;

            tot += first;
        }

        sum += tot;

        // secont digit off summuary to check validity.
        int second_of_sum = sum % 10;
        int digits;

        // Loop which gets only first two digits of number to recognize card issuer.
        while (first_digits > 10)
        {
            int dig = first_digits % 100;
            first_digits = first_digits / 10;
            digits = dig;
        }

        if (second_of_sum == 0)
        {
            if (counter == 15)
            {
                if (digits == 34 || digits == 37)
                {
                    printf("AMEX\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
            else if (counter == 16)
            {
                if (digits == 51 || digits == 52 || digits == 53 || digits == 54 || digits == 55)
                {
                    printf("MASTERCARD\n");
                }
                else if (digits / 10 == 4)
                {
                    printf("VISA\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
            else if (counter == 13)
            {
                if (digits / 10 == 4)
                {
                    printf("VISA\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
}
