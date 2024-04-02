// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, int tip)
{
    tax = 1 + tax/100;
    // printf("tax %f\n", tax);
    float f_tip = tip;
    f_tip = (f_tip/100) + 1;
    // printf("tip %f\n", f_tip);
    float total = bill * f_tip * tax;
    total /= 2;

    return total;
}
