#include <stdio.h>
#include <stdlib.h>

float average(int numbers[]);
void user_input();

int main() {

    return 0;
}

void user_input() {

    char ch;
    int n;
    int numbers[n];
    int index = 0;

    printf("Welcome to Simple Numbers\n");
    printf("Numbers please.\n");
    printf("Separate each number using spaces: ");
    while (ch = getchar()) {
        if (ch == ' ') {
            continue;
        } else if (ch == ',') {
            continue;
        } else {
            numbers[index] = atoi(ch);
        }
    }
}

float average(int numbers[]) {
    int *p;
    int sum = 0;
    int numbers_length = sizeof(numbers) / sizeof(numbers[0]);

    for (p = numbers; p < numbers_length; p++) {
        sum += *p;
    }

    return sum / numbers_length;
}
