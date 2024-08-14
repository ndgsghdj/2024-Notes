menu = ['OOLONG MILK TEA', 'EARL GREY MILK TEA', 'MATCHA LATTE', "YEO'S CHRYSANTHEMUM TEA"]
price = [4.9, 4.5, 6.9, 1.9]
bill = 0
print('Welcome to SSTea Inc!')

number_of_drinks = int(input("How many drinks would you like to order? "))

for _ in range(number_of_drinks):
    while True:
        order = input('What tea would you like to order? ').upper()
        if order not in menu:
            print("Order is not in menu!")
            continue
        break

    bill += price[menu.index(order)]
    print("Subtotal: ${}".format(bill))

if number_of_drinks > 3:
    bill *= 0.8

print('Your total bill is ${}.'.format(bill))
print('Thank you. Please come again!')
