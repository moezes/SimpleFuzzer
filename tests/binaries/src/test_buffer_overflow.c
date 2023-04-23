#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    volatile int modified;
    char buffer[24];

    if(argc > 1) {
        strcpy(buffer, argv[1]);
    } else {
        gets(buffer);
    }
    if(modified != 0) {
        printf("Overflown.");
    } else {
        printf("Failed.");
    }
    return 0;
}