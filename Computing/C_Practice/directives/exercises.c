#include <stdio.h>

#define CUBE(x) (x)*(x)*(x)
#define MOD(x, y) (x) % (y)

int main() {

    int n;
    int n1;
    
    printf("Enter two numbers: ");
    scanf("%d %d", &n, &n1);
    printf("%d^3 = %d\n", n, CUBE(n));
    printf("%d mod %d = %d\n", n, n1, MOD(n, n1));
}
