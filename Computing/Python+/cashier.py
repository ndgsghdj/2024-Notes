'''
Given a value N, and a list V[], find the smallest number of elements in V[] that sum up to N.
'''

memo = {}

def DP(S, V):

    # 1. Check if key exists in memo

    if S in memo:
        return memo[S]

    # 2. Base case? Termination condition

    if S == 0:
        return 0

    # 3. Go through EVERY possible option

    count = []

    for i in V:
        if S >= i:
            temp = 1 + DP(S - i, V)
            count.append(temp)

    # 4. Find which is the best solution
    sol = min(count)

    # 5. save it into memo
    memo[S] = sol

    # 6. Return solution

    return sol

print("Memo: ", DP(10, [1,2,5]))

