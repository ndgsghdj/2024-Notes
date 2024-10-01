nlist = ["Alden", "Belle", "Charles", "Dolly", "Elle", "Falken", "Grace", "Hacken"]
mlist = [56, 64, 23, 78, 53, 46, 98, 33] #1

to_find = input("Which name would you like to search for? ")

items = len(mlist) #11
num = 0
name_found = False
while name_found == False: #2
    while num < items: #5
        if nlist[num] == to_find: #3 #4
            print("{} score {} for the test".format(nlist[num], mlist[num])) #6
            name_found = True
            num = items #7
        elif num == items: #10
            print("{} is not in the list".format(to_find))
            name_found = True #8
            num = items
        else:
            num += 1 #9
