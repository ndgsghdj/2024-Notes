age = 0
height = float(0)
rejected = 0 #1
rider = 0
age = int(input("Please enter your age ")) #3
height = float(input("Please enter your height "))
while age != 0 and height != 0: #4
    if age <= 7 or age > 70 or height <= 1.3: #10
        if age < 7:
            print("You are too young to ride")
        if age > 70:#7
            print("You are too old to ride")
        if height <= 1.3:
            print("You are too short to ride")
        rejected = rejected + 1 #2
    else: #5
        print("You can ride the Roller Coaster")
        rider = rider + 1        #6
    age = int(input("Please enter your age "))
    height = float(input("Please enter your height "))
print("Number of people rejected ", rejected) #8
print("Number of riders ", rider) #9
