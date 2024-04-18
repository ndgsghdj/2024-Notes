def AddSum(k, n):
    if k == 0:
        return n
    else:
        return sum([AddSum(k-1, j) for j in range(1, n+1)])

