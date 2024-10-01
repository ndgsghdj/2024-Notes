while True:
    try:
        firstname = input("Please enter your first name: ")
        assert len(firstname) >= 3
        assert firstname.count(" ") == 0
        break
    except:
        print("First name has to be a word of three alphabets or more.")

while True:
    try:
        lastname = input("Please enter your last name: ")
        assert len(lastname) >= 3
        break
    except:
        print("Last name has to be a word of three alphabets or more.")

username = firstname[:3] + lastname[-3:]
print("Your username is {}".format(username))

while True:
    try:
        pin = input("Please enter a PIN: ")
        assert len(pin) == 6
        break
    except:
        print("PIN input must be 6 digits.")

while True:
    try:
        second_pin = input("Please re-enter your PIN: ")
        assert second_pin == pin
        print("Your PIN has been set.")
        break
    except:
        print("PIN entries do not match. Please repeat.")
