#Input
DS = input("DD MM YYYY:").split()
MM, Yr = int(DS[1]), int(DS[2]) #1

#Check if it is Leap year
leap_yr = False #2
if (Yr % 4) == 0:
    if (Yr % 100) == 0:
        if (Yr % 400) == 0:
            leap_yr = True
        else:
            leap_yr = False #6
    else:
        leap_yr = True #5
else: leap_yr = False #3

#Check for total days of the month
max_day = 31
if MM in [4, 6, 8, 11]:
    max_day = 30
elif MM == 2:
    max_day = 28

newDD, newMM, newYr = int(DS[0])+14, MM, Yr

#Check for day, month, year value overflow
if newDD > max_day:
    newDD = newDD % max_day #4
    newMM += 1
    if newMM > 12:
        newMM = 1
        newYr += 1 #7

#Output result
print("+14 days \nDD: {} MM: {} YYYY: {}".format(newDD,newMM,newYr)) #8
