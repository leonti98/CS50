#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int length = strlen(text);
    int sentence_counter = 0;
    int word_counter = 0;
    int letter_counter = 0;
    char c = 'a';

    for (int i = 0; i < length; i++)
    {
        c = text[i];
        // if character is . or ! or ? increase sentence_counet
        if (c == 46 || c == 33 || c == 63)
        {
            sentence_counter++;
        }
        // if character is space increase word_counter
        if (c == 32)
        {
            word_counter++;
        }
        // count number of letters
        if (c >= 'a' && c <= 'z')
        {
            letter_counter++;
        }
        else if (c >= 'A' && c <= 'Z')
        {
            letter_counter++;
        }
    }
    // add one because last word does not have space after.
    word_counter++;
    // L is the average number of letters per 100 words in the text
    float L = letter_counter / (float) word_counter * 100;
    // S is the average number of sentences per 100 words in the text
    float S = sentence_counter / (float) word_counter * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index <= 0)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
