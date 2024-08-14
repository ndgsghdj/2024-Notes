from random import randint
from collections import Counter

def dicerolls(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(randint(1, 10))

    return random_numbers

def dice_roll_combinations(n, m):
    results = [dicerolls(n) for  _ in range(m)]

    total = 0

    for i in results:
        for j in results:
            list1 = i
            list2 = j

    list1.sort()
    list2.sort()

    if list1 == list2:
        total += 1

    return total - 1
