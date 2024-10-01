p1_animals = []
p2_score = 0

while True:
    p1_animal = input("Player 1, please enter an animal: ")
    p1_animal = p1_animal.lower()
    p1_animals.append(p1_animal)

    more = input("Do you still want to enter an animal? [Y/N]")
    if more.upper() == "Y":
        continue
    elif more.upper() == "N":
        break

end_flag = False

while not end_flag:

    p2_guess = input("Player 2, please enter your guess: ")
    p2_guess = p2_guess.lower()

    if p2_guess in p1_animals:
        p2_score += 1
        p1_animals.pop(p1_animals.index(p2_guess))
    else:
        end_flag = True

print("Game Over!")
print("Player 2's score: {}".format(p2_score))
print("Animals still in the list: {}".format(", ".join(p1_animals)))

