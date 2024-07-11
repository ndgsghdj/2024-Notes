eggs_per_day = []

for i in range(7):
    array = []

    temp = input()

    temp_array = temp.split(',')
    for i in temp_array:
        while True:
            if (int(i) != 0) and (int(i) != 1):
                print("Input can only either be 0 or 1")
            else:
                break


    array = temp.split(",")

    array = [int(k) for k in array]
    eggs_per_day.append(sum(array))



for i in range(len(eggs_per_day)):
    print("Day {} \t {} egg(s)".format(i+1,eggs_per_day[i]))

print("Average number of eggs \t {}".format(int(round(sum(eggs_per_day)/4, 0))))
print("Total number of eggs for the week \t {}".format(sum(eggs_per_day)))


