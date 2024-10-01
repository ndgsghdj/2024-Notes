#include <stdlib.h>
#include <stdio.h>

int main() {

    int age = 27;
    double gpa = 3.4;
    char grade = 'A';

    int *pAge = &age;
    double *pGpa = &gpa;
    char *pGrade = &grade;

    /* Dereference pointer */

    printf("age's memory address: %d", *pAge);

    return 0;
}
