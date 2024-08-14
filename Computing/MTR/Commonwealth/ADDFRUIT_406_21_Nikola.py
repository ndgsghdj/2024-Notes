fruitlist = ["apple","orange","pear"]
stock = [1,1,1]
fruit = " "
while fruit != "":
    fruit = input("Enter fruit to add: ")
    if fruit in fruitlist:
        stock[fruitlist.index(fruit)] += 1
        print(stock[fruitlist.index(fruit)])
    else:
        fruitlist.append(fruit)
        stock.append(1)
print(fruitlist)
print(stock)
