firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[:3] + lastname
print("Your username is " + username)

while True:
    try:
        password = input("Please enter a password: ")
        assert len(password) >= 8
        break
    except:
        print("Password must be 8 characters or longer.")

while True: 
    try:
        password_2 = input("Please re-enter your password: ")
        assert password_2 == password
        print("Your password has been set.")
        break
    except:
        print("Password entries do not match. Please repeat the second entry of your password.")
