import time

def AddSum(k, n):
    if k == 0:
        return n
    val = 0
    for i in range(1, n+1):
        val += AddSum(k-1, i)
    return val

memo = {}

def AddSumSolution(k,n):

    if (k,n) in memo:
        return memo[(k,n)]

    if k == 0:
        return n
    val = 0

    for i in range(1, n+1):
        val += AddSumSolution(k-1, i)
        memo[(k,n)] = val

    return val

start = time.time()
print(AddSumSolution(14,14))
end = time.time()

print(f"time taken: {abs(end - start)}")
