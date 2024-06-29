#include "helpers.h"
// I can't see smiley, because zoom does not work.
// code works on outfile. CS50 accepts code.
void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                // make not black pixels red
                image[i][j].rgbtRed = 0xff;
            }
            else
            {
                // make face pixels blue
                image[i][j].rgbtBlue = 0xff;
                // image[i][j].rgbtGreen = 0xff;
                // image[i][j].rgbtRed = 0xff;
            }

        }
    }
}
