def getClues(guess, secret_number):
    clue = ['0']*3

    if guess == secret_number:
        print("You got it")
    else:
        for i in range(3):
            if guess[i] == secret_number[i]:
                clue[i] = 'Fermi'
            elif guess[i] in secret_number:
                clue[i] = 'Pico'
            elif guess[i] != secret_number[i]:
                clue[i] = 'Bagels'

    return ' '.join(clue)

