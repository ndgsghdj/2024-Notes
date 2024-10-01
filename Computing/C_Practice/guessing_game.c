#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main() {
    
    srand(time(NULL));
    int random_number = rand() % 100;
    int guesses = 3;
    int guess;

    printf("You have %d guesses. Use them wisely!\n", guesses);

    while(guesses > 0) {

        printf("Enter a guess: ");
        scanf("%d", &guess);
        
        if (guess < random_number) {
            printf("Higher\n");
            guesses--;
            printf("You have %d guesses left!\n", guesses);
        } else if (guess > random_number) {
            printf("Lower\n");
            guesses--;
            printf("You have %d guesses left!\n", guesses);
        } else {
            printf("You got it!\n");
            break;
        }

    }

    printf("The secret number was %d\n", random_number);

    return 0;
}
