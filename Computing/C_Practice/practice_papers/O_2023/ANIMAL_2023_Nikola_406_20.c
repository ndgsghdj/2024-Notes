#include <stdio.h>
#include <ctype.h>

int main() {
    int num_of_animals = 5;
    char *p1_animals;
    char *p2_guess;

    for (int i = 0; i < num_of_animals; i++) {
        printf("Player 1, please enter an animal: ");
        scanf("%s", p1_animals);

        for (int i = 0; p1_animals[i]; i++) {
            p1_animals[i] = tolower(p1_animals[i]);
        }
        
        printf("Player 2, please enter a guess: ");
        scanf("%s", p2_guess);

        for (int i = 0; p2_guess[i]; i++) {
            p2_guess[i] = tolower(p2_guess[i]);
        }
        
    }
}
