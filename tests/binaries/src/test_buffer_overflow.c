#include <stdio.h>

int main(int argc, char** argv) {
    volatile int modified;
    char buffer[24];
    gets(buffer);
    if(modified != 0) {
        printf("Overflown.");
    } else {
        printf("Failed.");
    }
}