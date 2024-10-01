#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}

int main () {
    printf("Maximum of {2,3}: %d", max(2,3));
    return 0;
}
