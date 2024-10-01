#include <stdlib.h>
#include <stdio.h>

int gcd(int m, int n) {
    if (m % n == 0) {
        return n;
    }

    return gcd(n, m % n);
}

int main() {
    
    int m;
    int n;

    printf("Enter two integers: ");
    scanf("%d %d", &m, &n);
    printf("GCD of the two numbers: %d\n", gcd(m, n));

    return 0;
}
