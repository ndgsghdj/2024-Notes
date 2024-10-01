total_eggs = []
hen_total = [0] * 4
day = 1

while True:
    if day == 8:
        break
    day_eggs = input("Eggs for day {}: ".format(day))
    day_eggs = day_eggs.split(", ")
    day_eggs = [int(k) for k  in day_eggs]
    check_flag = False
    for hen in day_eggs:
        try:
            assert hen == 0 or hen == 1
        except:
            print("Egg laid by one hen must be either 1 or 0 each day.")
            check_flag = True
            break

    if check_flag:
        continue

    total_eggs.append(sum(day_eggs))
    
    for i in range(4):
        hen_total[i] += day_eggs[i]

    day += 1

for i in range(1, 8):
    print("Day {}\t {} egg(s)".format(i, total_eggs[i-1]))

print("Average number of eggs             {}".format(int(round(sum(total_eggs)/4, 0))))
print("Total number of eggs for the week  {}".format(sum(total_eggs)))

for i in range(4):
    if hen_total[i] < 4:
        print("Hen {}   {} eggs(s)".format(i+1, hen_total[i]))
    
