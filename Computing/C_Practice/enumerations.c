#include <stdio.h>
#include <stdlib.h>

/* enum suit {CLUBS, DIAMONDS, HEARTS, SPADES}; */

typedef enum {CLUBS, DIAMONDS, HEARTS, SPADES} Suit; /* Actually just integers under the hood */
Suit s1, s2;

typedef struct {
    enum {INT_KIND, DOUBLE_KIND} kind;
    union {
        int i;
        double d;
    } u;
} Number;
