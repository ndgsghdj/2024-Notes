p1_animals = []

while True:
    p1_animal = input("Player 1, please enter an animal: ")
    p1_animal = p1_animal.lower()
    p1_animals.append(p1_animal)

    more = input("Do you still want to enter an animal? [Y/N]")
    if more.upper() == "Y":
        continue
    elif more.upper() == "N":
        break

p2_guess = input("Player 2, please enter your guess: ")
p2_guess = p2_guess.lower()
