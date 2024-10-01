colour_list = ["red", "green", "blue", "orange", "purple", "yellow"]
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_to_find)
item_number = 0
colour_found = False
while colour_found == False: #5
    while item_number < items: #4
        if item_number == items - 1: #9
            print("The colour is not in the list.")
            colour_found = True
            item_number = items
        elif colour_list[item_number] == colour_to_find: #2 #3
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") #1 #6
            colour_found = True
            item_number = items #8
        else:
            item_number = item_number + 1 #7 
