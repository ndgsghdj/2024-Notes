import random

NUM_DIGITS = 3

MAX_GUESS = 10

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def inGuess():
    validation_flag = True

    guess = ''
    while validation_flag:
        guess = input("Give your guess: ")
        if len(guess) == 3 and guess.isnumeric():
            validation_flag = False
        else:
            print("Guess must be a 3-digit number!")

    return guess
