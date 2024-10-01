flag = True
list_name_totals = [] #1
count = 1

while flag:
    total = 0 #8
    name = input("Please enter the Player's name: ")
    length_string = len(name) #2
    name = name.upper()
    print("You are player " + str(count))
    # for x in range(length_string - 1): #missing
    for x in range(length_string):
        char = name[x]
        value = ord(char) #3
        total = total + value #4
    list_name_totals.append(total) #5
    print("Your total is " + str(total))
    more = input("Would you like to enter another player's name? Enter Yes or No. ")
    if more == "No":
        flag = False
    else:
        count +=1
highest = max(list_name_totals) #6
for x in range(len(list_name_totals)): #7
    if list_name_totals[x] == highest:
        position = x
print("The highest value is " + str(highest) + " and that is player " + str(position + 1)) #9
