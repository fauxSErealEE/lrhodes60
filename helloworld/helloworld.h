#include <stdio.h>
#include <conio.h>

void end_pause();

void end_pause()
{
    /* Makes program pause before exiting */
    printf("\nPress any key to continue...");
    char end = getche();
}