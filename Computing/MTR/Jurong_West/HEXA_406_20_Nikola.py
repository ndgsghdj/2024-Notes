#Task 3

flag = True #1
denary = 0
hexa = ('A','B','C','D','E','F')

value = input("Enter the 4-digit hexadecimal value:")
reverse = value[::-1] #2
print(reverse)

for i in range(4): #6
    if reverse[i].isdigit(): #5
        print(reverse[i])
        denary = denary + int(reverse[i])*(16**i)
    elif reverse[i] in hexa:
        print(reverse[i])
        if reverse[i]=="A":
            denary = denary + 10*(16**i) #7
        elif reverse[i]=="B":
            denary = denary + 11*(16**i)
        elif reverse[i]=="C":
            denary = denary + 12*(16**i)
        elif reverse[i]=="D":
            denary = denary + 13*(16**i)
        elif reverse[i]=="E":
            denary = denary + 14*(16**i)
        else: #4
            denary = denary + 15*(16**i)
    else:
        flag = False #3

if flag == True: #8
    print("The denary value is", denary)
else:
    print("Invalid hexadecimal value")
