#include <stdlib.h>
#include <stdio.h>

int main() {

    int a,b,c,d;
    int postman[4] = {0,0,0,0};
    int days[5];

    for (int i = 0; i <= 4; i++) {
        for (;;) {
            printf("Enter parcels collected by the team: ");
            scanf("%d,%d,%d,%d", &a, &b, &c, &d);
            if ((0 <= a && a <= 10 && 0 <= b && b <= 10 && 0 <= c && c <= 10 && 0 <= d && d <= 10)) {
                break;
            }

            printf("Error - Please enter number 0 to 10\n");
        }

        days[i] = a + b + c + d;
        
        postman[0] += a; postman[1] += b; postman[2] += c; postman[3] += d;
    }
    
    /*
    for (int i = 0; i < 5; i++) {
        printf("Day %d: The team collected %d parcel(s).\n", i+1, days[i]);
    }
    */

    int *ptr = days;
    for (int i = 0; ptr < days + 5; ptr++, i++) {
        printf("Day %d: The team collected %d parcel(s).\n", i + 1, *ptr);
    }

    int sum = 0;

    int *p = days;
    for (int i = 0; p < days + 5; p++, i++) {
        sum += *p;
    }

    printf("Average number of parcels \t %d\n", sum / 5);
    printf("Total number of parcels for the week \t %d\n", sum);

    int *ptr_post = postman;

    for (int i = 0; ptr_post < postman + 4; ptr_post++, i++) {
        if (*ptr_post < 30) {
            printf("Postman %d collected %d parcels this week.\n", i+1, *ptr_post);
        }
    }

    return 0;
}