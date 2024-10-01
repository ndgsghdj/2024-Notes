name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #5
flag = True
while flag == True: #2
    name = input("Enter student's name: ") #1
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #3
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #4
    count += 1
    if mark >= 75: #6
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #7
    more = input('Would you like to enter another score, Y or N?: ') #8
    if more == 'N':
        flag = False
        
average = round(sum(mark_list)/len(mark_list), 2) #10
num_dist = len(dist_list)
num_fail = len(fail_list)

print("You entered " + str(count) + " scores.") #9
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))
