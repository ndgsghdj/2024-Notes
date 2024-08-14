fruitlist = ["apple","orange","pear"]
stock = [1,1,1]
fruit = " "
while fruit != "":
    fruit = input("Enter fruit to remove from stock: ")
    stock[fruitlist.index(fruit)] -= 1
    if stock[fruitlist.index(fruit)] == 0:
        break
print(fruitlist)
print(stock)
