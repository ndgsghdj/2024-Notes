p1_word = ""

while True:
    try:
        p1_word = input("Enter a word with 10 characters or less: ")
        assert len(p1_word) <= 10
        break
    except:
        print("Word must have less than or equal to 10 characters.")

for _ in range(10):
    p2_guess = input("Guess a lowercase letter: ")

    found = False
    for i in range(len(p1_word)):
        if p1_word[i] == p2_guess:
            print("It is letter {} in the word.".format(i))
            found = True
            break

    if found:
        p2_guess_choice = input("Do you want enter the word entered by player 1? [yes/no] ")
        if p2_guess_choice == "yes":
            p2_guess_word = input("What is the word entered by player 1? ").lower()

            if p2_guess_word == p1_word:
                print("That is the correct word. You win!")
                break
            else:
                print("That is not the correct word.")

    if not found:
        print("That letter is not in the word.")

print("You have now entered 10 letters.")
p2_guess_word = input("What is the word entered by player 1? ").lower()

if p2_guess_word == p1_word:
    print("That is the correct word. You win!")
else:
    print("That is not the correct word. Player 1 wins!")
