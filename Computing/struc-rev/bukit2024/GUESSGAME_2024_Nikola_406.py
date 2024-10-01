import random

def select_word(w_list):
    r_num= random.randint(0,len(w_list)-1)
    word = w_list[r_num]
    return word

def check_word(word1, word2):
    return word1 == word2

def check_letter(word, letters):
    new_word = word
    new_word_list = list(new_word)

    for c in word:
        if c not in letters:
            idx = new_word.find(c)
            new_word_list[idx] = "_"

    new_word = "".join(new_word_list)

    return new_word

words = ["house", "grass", "green", "block"]
guesses = 6
win = False

word_selected = select_word(words)

for i in range(guesses):
    if win:
        break

    choice = input("Do you want to guess a word or a letter? [W/L] ")

    if choice == "W":
        while True:
            try:
                word = input("Enter a word: ")
                for c in word:
                    assert c.isalpha()
                    assert c != " "
                break
            except:
                print("Word entered has to be a singular word with letters only.")

        if word == word_selected:
            print("Good Job! You guessed the word!")
            win = True

    else:
        letters = []
        while True:
            try:
                letter = input("Enter a letter: ")
                assert letter.isalpha()
                break
            except:
                print("Letter must be a valid English letter in the alphabet.")
        letters.append(letter)
        print("Progress of word: {}".format(check_letter(word_selected, letters)))

if not win:
    print("Game over!")
