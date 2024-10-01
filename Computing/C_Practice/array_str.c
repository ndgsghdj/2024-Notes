#include <string.h>
#include <stdio.h>

int main() {

   /* char planet[][8];*//* Space is wasted */
    char *planets[] = {
        "Mercury", "Venus", "Earth",
        "Mars", "Jupiter", "Saturn",
        "Uranus", "Neptune", "Pluto"
    }; /* Each element of the array is a pointer to a null-terminated string */

    for (int i = 0; i < 9; i++) {
        if (planets[i][0] == 'M') {
            printf("%s begins with M\n", planets[i]);
        }
    }

    

    return 0;
}
