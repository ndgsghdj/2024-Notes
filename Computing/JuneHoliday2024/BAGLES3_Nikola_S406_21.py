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

def getClues(guess, secret_number):
    clue = ['0']*3

    if guess == secret_number:
        return "You got it!"
    else:
        for i in range(3):
            if guess[i] == secret_number[i]:
                clue[i] = 'Fermi'
            elif guess[i] in secret_number:
                clue[i] = 'Pico'
            elif guess[i] != secret_number[i]:
                clue[i] = 'Bagels'

    return ' '.join(clue)

print("Welcome to 'Bagels'!")
print("You have 10 guesses.")

guesses = 10
guess_flag = False

while not guess_flag:
    secret_number = getSecretNum()
    guess = inGuess()
    clue = getClues(guess, secret_number)
    if clue == "You got it!":
        print(clue)
        guess_flag = True
    else:
        print(clue)
        guesses -= 1
        print("Guesses left: {}".format(guesses))
    if guesses == 0:
        print("The answer is: {}".format(secret_number))
    break
