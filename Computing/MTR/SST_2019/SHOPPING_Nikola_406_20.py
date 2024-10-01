#input items in a shopping cart and the quantity

different_items = 5
shopping_cart = []
shopping_item = []
for i in range(different_items):
    new_item = input("Please enter an item: ")

    while True:
        try:
            new_quantity = input("Please enter the quantity of item: ")
            assert int(new_quantity) > 0
            break
        except:
            print("Please re-enter a positive quantity.")

    price = float(input("Please enter the unit cost of the item: "))

    shopping_item = [new_item, int(new_quantity), price * int(new_quantity)]
    shopping_cart.append(shopping_item)
print(shopping_cart)

largest_quantity = 0
smallest_quantity = float('inf')
sequence = 0
sequence_smallest = 0
for j in range(different_items):
    if shopping_cart[j][1] > largest_quantity:
        sequence = j
        largest_quantity = shopping_cart[j][1]
    elif shopping_cart[j][1] < smallest_quantity:
        sequence_smallest = j
        smallest_quantity = shopping_cart[j][1]

total_cost = 0

for item in shopping_cart:
    total_cost += item[2]

print("The item with the greatest quantity is ",shopping_cart[sequence][0])
print("")
print("There are ",largest_quantity, shopping_cart[sequence][0], "in total.")
print("Total cost: {}".format(total_cost))
