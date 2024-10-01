#include <stdio.h>

char *cake_list = "ABCDEFGH";

int get_price(char option) {
    int cake_length = 8;
    int position = 0;
    int price_list[8] = {
        25,22,38,35,15,40,53,20
    };
    
    char *p;
    for (p = cake_list; *p != '\0'; p++) {
        if (*p == option) {
            break;
        } 
        position++;
    }

    return price_list[position];

}

char get_input() {
    char choice;

    char *p;
    for (;;) {
        printf("Enter the choice of cake: ");
        scanf(" %c", &choice);
        for (p = cake_list; *p != '\0'; p++) {
            if (*p == choice) {
                printf("%c\n", choice);
                return choice;
            }
        }
        printf("Enter an uppercase letter between A to H only\n");

    }
}

void get_order() {
    char choice;
    char more_purchase;

    int subtotal = 0;
    float gst;
    float total;

    for (;;) {
        choice = get_input();

        total += get_price(choice);
        subtotal = total;

        printf("More purchase? Y or N: ");
        scanf(" %c", &more_purchase);

        if (more_purchase == 'N') {
            break;
        }
        
    }

    gst = 0.07 * subtotal;
    total += gst;

    printf("Subtotal       $ %d\n", subtotal);
    printf("GST            $ %.2f\n", gst);
    printf("Total          $ %.2f\n", total);
}

int main() {
    get_order();

    return 0;
}
