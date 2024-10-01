#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NAME_LEN 100
#define FIRST_NAME_LEN 100
#define LAST_NAME_LEN 100

struct part { /* Structure tag */
    int number;
    char name[NAME_LEN+1];
    int on_hand;
};

void print_part(struct part p);

int main() {

    struct part part1 = {528, "Disk drive", 10};
    struct part part2;

    part2 = part1; /* legal, both parts have the same type */

    typedef struct { /* Structure type */
        int number;
        char name[NAME_LEN+1];
        int on_hand;
    } Part;

    Part part3, part4;

    print_part(part1);

    return 0;
}

void print_part(struct part p) {
    printf("Part number: %d\n", p.number);
    printf("Part name: %s\n", p.name);
    printf("Quantity on hand: %d\n", p.on_hand);
}

struct part build_part(int number, const char *name, int on_hand) {
    struct part p;

    p.number = number;
    strcpy(p.name, name);
    p.on_hand = on_hand;
    return p;
}

void f(struct part part1) {
    struct part part2 = part1;
}

/** Nested Structures **/

struct person_name {
    char first[FIRST_NAME_LEN+1];
    char middle_initial;
    char last[LAST_NAME_LEN+1];
};

struct student {
    struct person_name name;
    int id, age;
    char sex;
} student1, student2;

/** Arrays of Structures **/

struct part inventory[100];

print_part(inventory[i]);
