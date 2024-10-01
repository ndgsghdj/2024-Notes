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
            print("Enter an uppercase letter between A to H only")
            continue
        else:
            break

    return choice
