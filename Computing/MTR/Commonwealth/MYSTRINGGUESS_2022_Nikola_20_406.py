string = ""
for i in range(3):
    letter_ord = int(input("Player 1, enter number between 65 to 90 inclusive: "))
    while letter_ord < 65 or letter_ord > 90: #1 #8
        print("Number entered is not between 65 to 90 inclusive.")
        letter_ord = int(input("Player 1, enter number between 65 to 90 inclusive: ")) #10
    string = string + chr(letter_ord) #2

for i in range(5):
    found = False #9
    guess_letter = input("Player 2, enter a letter: ").upper()  #3
    for j in range(len(string)):
        if string[j] == guess_letter:
            print("Your letter is found in the string. Position number is " + str(j + 1)) #4 #7
            found = True #5
    if found == False:
        print("Your letter is not inside the string.")

guess_str = input("Player 2, guess the 3-letter string: ")
if guess_str == string: #6
    print("Congratulations, you have managed to guess the string.")
else:
    print("You did not manage to guess the string.")
