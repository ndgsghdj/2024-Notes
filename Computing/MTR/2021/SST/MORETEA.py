def drinkOption(base_cost) : #1
    add_cost = base_cost
    reject = False #2
    print('Small +$0, Medium +$1.00, Large +$1.50') #3
    size = input("Upsize? [S, M, L] : ").upper()
    sugar_level = input("Sugar level [0, 25, 50, 75, 100] : ")
    pearls = input("Add Pearls +$0.50  [Y]es [N]o : ").upper()
    jelly = input("Add Jelly +$1.00 [Y]es [N]o : ").upper()
    if size == "M": #4
        add_cost += 1.0
    elif size == "L" :
        add_cost += 1.5
    elif size == "S" :
        add_cost += 0
    else: #5
        reject = True
    if int(sugar_level) not in [0, 25, 50, 75, 100]: #8
        reject = True
    if pearls == "Y":
        add_cost += 0.50 #6
    elif pearls not in "YN":
        reject = True
    if jelly == "Y": #7
        add_cost += 1.0
    elif jelly not in "YN":
        reject = True
    if reject:
        return base_cost
    return add_cost #6

menu = ["OOLONG MILK TEA", "EARL GREY MILK TEA", "MATCHA LATTE"]
price = [4.9, 4.5, 6.9]
print("Welcome to SSTea Inc!")
order = input("What tea would you like to order? ")
bill = price[menu.index(order)]
bill = drinkOption(bill)
print("Your total bill is ${}.".format(bill))
print("Thank you. Please come again!")
