#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Student {
    char name[50];
    char major[50];
    int age;
    double gpa;
};

int main() {

    struct Student student1;
    student1.age = 22;
    student1.gpa = 3.2;
    strcpy(student1.name, "Nikola");
    strcpy(student1.major, "Business");

    printf("%f", student1.gpa);
    printf("%s", student1.name);

    struct Student student2;
    student2.age = 22;
    student2.gpa = 3.2;
    strcpy(student2.name, "Jim");
    strcpy(student2.major, "Business");

    return 0;
}
