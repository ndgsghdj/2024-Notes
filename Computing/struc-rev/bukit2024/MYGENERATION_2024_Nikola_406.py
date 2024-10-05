CURRENT_YEAR = 2024
list_phone = [] #1
pioneer = 0 
merdeka = 0

year = int(input("Please enter year of birth:" ))
age = CURRENT_YEAR - year
oldest = age
result = input("Were you a Singapore citizen before 31 December 1996? (Y/N) or press enter to exit program:").upper()

while result != "":
    if age >= 65 and result == "Y": #3 #8
        if age >= 75: #5
            print("You qualify for the Pioneer Generation Package")
            pioneer = pioneer + 1

        elif age >= 65:
            print("You qualify for the Merdeka Generation Package")
            merdeka = merdeka + 1 #8

        phone_num = input("Please enter your phone number: ")
        list_phone.append(phone_num) #4
        if age > oldest: #2
            oldest = age

    else:
        print("You currently do not qualify for any packages")

    year = int(input("Please enter year of birth:" )) #7
    age = CURRENT_YEAR - year #9
    result = input("Were you a Singapore citizen before 31 December 1996? (Y/N) or press enter to exit program:").upper()

print("Total eligibility: " + str(pioneer) + " Pioneer Generation package and " + str(merdeka) + " Merdeka Generation package") #6
print("Age of the oldest applicant: ", oldest)
print("List of phone numbers", list_phone)
