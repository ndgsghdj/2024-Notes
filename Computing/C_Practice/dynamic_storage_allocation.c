#include <stdlib.h>
#include <stdio.h>

int main() {
    void *p;
    p = malloc(10000); 
    p = (char *) malloc(10000); /* void pointer converted to char pointer */

    /* malloc(n + 1): allow room for the null character. */

    if (!p) {
        printf("");
    }
}
