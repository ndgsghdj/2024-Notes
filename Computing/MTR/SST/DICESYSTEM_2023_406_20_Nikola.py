from random import randint

def dicerolls(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(randint(1, 10))

    return random_numbers

while True:

    n = int(input("Number of dice to roll: "))
    result = dicerolls(n)
    print("Rolls: {}".format(result))

    for _ in range(len([i for i in result if i == 1])):
        print("1 rolled! Highest success removed: {}".format(result.pop(result.index(1))))

    dice_rolls = len([i for i in result if i == 10])

    if dice_rolls >= 1:
        while True:
            try:
                x = int(input("Number of additional dice you would like to roll: "))
                assert 0 <= x <= dice_rolls
                break
            except:
                print("Number of additional dice rolls must be a positive integer less than {}.".format(dice_rolls))

        additional_dice_rolls = dicerolls(x)
        result += additional_dice_rolls

        for i in additional_dice_rolls:
            if i == 1:
                print("1 rolled! Highest success removed: {}".format(result.pop(result.index(1))))

        print("Rolls: {}".format(result))

        if len([i for i in result if i > 6]) > 0:
            print("Success")
        else:
            print("Fail")

    repeat = input("Do you want to enter a new number of dice to roll? Y/N ")
    if repeat == "N":
        break
    else:
        pass

