# 2024 BVSS Prelim T4 GUESSGAME
import random

def select_word(w_list):
    r_num= random.randint(0,len(w_list)-1)
    word = w_list[r_num]
    return word

# Q11 GUESSWORD

def check_word(word1, word2):
    return word1 == word2

# Q12 GUESSLETTER

def check_letter(word, list_letters):
    current_progress = ["_"] * len(word)

    for letter in list_letters:
        for i in range(len(word)):
            if letter == word[i]:
                current_progress[i] = letter

    return "".join(current_progress)

# Q13 GUESSGAME

word_list = ["house", "grass", "green", "block"]
hidden_word = select_word(word_list)
max_guess = 6
current_attempt = 1
user_letters = []

while current_attempt <= 6:
    print("Attempt {}".format(current_attempt))
    print("1. Guess Word\n2. Guess Letter")
    choice = int(input())

    if choice == 1:
        word_input = input("Enter a word: ")
        while not(word_input.isalpha()):
            print("Invalid word, it must contain letters only.")
            word_input = input("Re-enter a word: ")

        if check_word(word_input, hidden_word):
            break

    elif choice == 2:
        letter_input = input("Enter a letter: ")
        while not(letter_input.isalpha() and len(letter_input) == 1):
            print("Letter must be in the alphabet.")
            letter_input = input("Re-enter a letter: ")
        
        user_letters.append(letter_input)
        current_progress = check_letter(hidden_word, user_letters)
        print("Current progress: {}".format(current_progress))
    
    current_attempt += 1

if current_attempt <= 6:
    print("Congrats! You guessed it correctly on attempt {}".format(current_attempt))
else:
    print("Game over!")
