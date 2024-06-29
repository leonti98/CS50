#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // check if correct amount of arguments were given
    if (argc != 2)
    {
        printf("Usage ./recover filename\n");
        return 1;
    }
    // open file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("file with name %s was not found\n", argv[1]);
        return 1;
    }
    // create necessary variables
    int BLOCK_SIZE = 512;
    uint8_t buffer[BLOCK_SIZE];
    int counter = 0;
    char name[8];
    bool found = false;
    FILE *img = NULL;
    // read chunck of 512 bytes from file
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // check if block starts with jpeg signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if file is already open close
            if (found)
            {
                fclose(img);
            }
            // else indicate that file was found
            else
            {
                found = true;
            }
            // generate and create new file
            sprintf(name, "%03i.jpg", counter);
            img = fopen(name, "w");
            // if file cound not be open report
            if (img == NULL)
            {
                fclose(file);
                printf("caould not create %s\n", name);
                return 1;
            }
            printf("Found JPEG signature at position %d\n", counter);
            printf("Creating file: %s\n", name);
            // inrease counter to generate new file name
            counter++;
        }
        // if jpeg was found write data to new file
        if (found)
        {
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }
    }
    // if jpeg was found, but new signature was not, continue writing
    if (found)
    {
        if (!(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0))
        {
            // If not, close the last image file
            fclose(img);
            printf("closed file: %s\n", name);
            found = false; // Reset found flag to indicate no image file is currently open
        }
        else
        {
            // If yes, continue writing to the current image file
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }
    }
    fclose(file);
    return 0;
}
