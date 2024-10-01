import math

def get_price(option):
    cake_list = ["A", "B", "C", "D","E","F","G","H"]
    price_list = [25, 22, 38, 35, 15, 40, 53, 20]
    position = cake_list.index(option)
    return price_list[position]

def get_input():
    choice = ''
    while True:
        choice = input("Enter the choice of cake: ")
        if choice not in "ABCDEFGH":
            continue
        else:
            break

    return choice

def get_order():
    total = 0
    subtotal = 0
    gst = 0

    while True:
        choice = get_input()
        subtotal += get_price(choice)
        gst = 0.07 * subtotal
        total = subtotal + gst
        more = input("More purchase? Y or N: ")

        if more.upper() == "N":
            break
        else:
            pass

    print("\nSubtotal     $ {}".format(subtotal))
    print("GST          $ {}".format((round(gst, 2))))
    print("Total        $ {}".format(round(total, 2)))
    print("\nThank you!")

get_order()
