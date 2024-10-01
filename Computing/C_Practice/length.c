#include <stdlib.h>
#include <stdio.h>

int main() {

    int len = 0;
    char message[2000];

    printf("Message: ");
    fgets(message, sizeof(message), stdin);

    for (int i = 0; message[i] != '\n'; i++) {
        len++;
    }

    printf("Length of message: %d\n", len);

    return 0;
}
