memo = {}

def count_combinations(K, N):
    global memo
    if K == 0:
        return 1
    if K < 0 or N < 1:
        return 0

    if (K, N) in memo:
        return memo[(K, N)]

    combinations = 0
    for crate_weight in range(N, K+1):
        combinations += count_combinations(K - crate_weight, N, memo)
    memo[(K, N)] = combinations
    return combinations

print(count_combinations(20, 5, memo))
