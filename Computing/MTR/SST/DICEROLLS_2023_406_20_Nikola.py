from random import randint

def dicerolls(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(randint(1, 10))

    return random_numbers
