#include <stdlib.h>
#include <stdio.h>

int main() {

    int array[] = {1,2,3};

    printf("%lu", sizeof(array)/sizeof(array[0]));

    return 0;
}
