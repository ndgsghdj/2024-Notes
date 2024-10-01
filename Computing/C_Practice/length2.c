#include <stdio.h>
#include <stdlib.h>

int main() {

    int len = 0;
    char ch;

    printf("Message: ");
    ch = getchar();

    while (ch != '\n') {
        len++;
        ch = getchar();
    }

    printf("Length of message: %d\n", len);

    return 0;
}
