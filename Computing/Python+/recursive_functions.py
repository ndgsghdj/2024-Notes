# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
