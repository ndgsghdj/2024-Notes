#include <stdio.h>

int main(int argc, char *argv[]) { 
    /* argc - Argument count, number of command-line arguments
       argv - Argument vectory, array of pointers to command-line arguments */
    int i;
    for (i = 1; i < argc; i++) {
        printf("%s\n", argv[i]);
    } /* Prints the command-line arguments line by line */

    char **p; /* pointer to a pointer to a char */
    for (p = &argv[1]; *p != NULL; p++) {
        printf("%s\n", *p);
    }
    /*
     * p = &argv[1] is ok because argv[1] is a pointer to a char, so &argv[1] is a pointer to a pointer
     * *p != NULL is ok since *p and NULL are both pointers.
    */
    
}
