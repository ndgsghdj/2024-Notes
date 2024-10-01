create = input("Create account (True/False): ")
if create == "True": #2
    for i in range(1,4): #3
        print("Attempt:", i) #4
        specialChar = None
        numbers = None
        upperCase = None
        pw = input("Password: ")
        pw_2nd = input("Retype password: ") #1

        if not(len(pw) >= 10 and pw == pw_2nd): #5
            print("Passwords do not match or password too short.")
            continue #6

        for c in pw:
            if c in "!@#$%&*": #7
                specialChar = True
            if c.isnumeric(): #8
                numbers = True
            if c.isupper(): #9
                upperCase = True
        if upperCase and numbers and specialChar:
            encrypt_pw = ""
            for c in pw:
                encrypt_pw += str(ord(c)) #10
            print("encrypted password:", encrypt_pw)
            break

        print("Password does not meet conditions.")
        continue
