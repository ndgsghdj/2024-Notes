"""
20
> Split to k/2
-> 5,6,7,8,9,10
-> 15,14,13,12,11,10

15
> Split to k/2
-> 5,6,7
-> 10,9,8

14
> Split to k/2
-> 5,6,7
-> 9,8,7

13
> Split to k/2
-> 5,6
-> 8,7

...
"""

def count_combinations(k, n):
    # Base case
    if k < n:
        return 0

    count = 1
    for i in range(n, k//2+1):
        count += count_combinations(k-i, i)
    return count

print(count_combinations(20,5))


