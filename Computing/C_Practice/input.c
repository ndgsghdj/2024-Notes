#include <stdio.h>

int main() {

    char name[20];
    int age;
    char grade;

    printf("Enter your name: ");
    fgets(name, 20, stdin);
    printf("Your name is %s\n", name);

    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Your age is %d\n", age);

    printf("Enter your grade: ");
    scanf("%c", &grade);
    printf("Your grade is %c\n", grade);

    return 0;
}
