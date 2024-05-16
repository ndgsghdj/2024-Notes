import math

def signal_loss(x):
    count = 0

    for i in range(1, int(math.sqrt(x)) + 1):
        if i ** 2 < x:
            count += 1

    return count

def signal_loss2(x):

    n = math.ceil(math.sqrt(x))

    return n-1

cont = True

while cont:
    x = int(input("Enter an integer: "))

    print("There are {} stepss of signal loss at distance {}".format(signal_loss(x), x))

    temp = input("Enter 'Q' to quit or any key to continue")

    if temp.upper() == "Q":
        temp = False

