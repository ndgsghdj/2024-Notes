#include <stdio.h>

int sum(int n) {
    if (n == 1) {
        return n;
    }

    return n + sum(n-1);
}

int main() {
    int n;
    printf("Enter the value of n: ");
    
    scanf("%d", &n);
    int sum_n = sum(n); 

    printf("%d\n", sum_n);
    return 0;
}
