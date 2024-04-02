#include "helpers.h"
#include "stdio.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            int average = round((red + green + blue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // printf("%i\n", image[i][j].rgbtRed);
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // allocate space for one row of pixels
        int *pixelsRed = malloc(width * sizeof(int));
        int *pixelsGreen = malloc(width * sizeof(int));
        int *pixelsBlue = malloc(width * sizeof(int));
        // store all pixels from current row in new variable
        for (int j = 0; j < width; j++)
        {
            pixelsRed[j] = image[i][j].rgbtRed;
            pixelsGreen[j] = image[i][j].rgbtGreen;
            pixelsBlue[j] = image[i][j].rgbtBlue;
        }
        // assign pixels backwards
        for (int t = 0; t < width; t++)
        {
            image[i][t].rgbtRed = pixelsRed[width - t - 1];
            image[i][t].rgbtGreen = pixelsGreen[width - t - 1];
            image[i][t].rgbtBlue = pixelsBlue[width - t - 1];
        }
        free(pixelsRed);
        free(pixelsGreen);
        free(pixelsBlue);
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // copy image into new variable
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtBlue = image[i][j].rgbtBlue;
        }
    }
    // blur image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum[3];
            sum[0] = 0;
            sum[1] = 0;
            sum[2] = 0;
            int devider = 0;

            // loop through pixels around and itself
            for (int h = -1; h < 2; h++)
            {
                for (int w = -1; w < 2; w++)
                {
                    // if pixels are not out of image range
                    if (i + h >= 0 && j + w >= 0 && i + h < height && j + w < width)
                    {
                        devider++;
                        // sum pixels around
                        sum[0] += copy[i + h][j + w].rgbtRed;
                        sum[1] += copy[i + h][j + w].rgbtGreen;
                        sum[2] += copy[i + h][j + w].rgbtBlue;
                    }
                }
            }
            // make curren pixel color equal to average
            // multiplying by 1.0 to make number float, because round did not work correctly
            image[i][j].rgbtRed = round(1.0 * sum[0] / devider);
            image[i][j].rgbtGreen = round(1.0 * sum[1] / devider);
            image[i][j].rgbtBlue = round(1.0 * sum[2] / devider);
        }
    }
    return;
}
