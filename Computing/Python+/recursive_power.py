"""
n^e = 1 <=> e = 0
    = n^(e/2) * n^(e/2) <=> e is even
    = n * n^((e-1)/2) * n^((e-1)/2)
add when e < 0
"""

def power(n, e):
    if e==0: return 1
    temp = power(n, e//2)
    if e % 2 == 0:
        return temp * temp
    else:
        return n * temp * temp

# Can you modify this and make sure it works when e < 0?
