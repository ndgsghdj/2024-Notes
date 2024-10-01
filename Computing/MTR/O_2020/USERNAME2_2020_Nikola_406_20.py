usernames = ["TSt01"]

while True:
    first_name = input("First name: ")
    last_name = input("Last name: ")
    year_of_birth = input("Year of birth: ")

    username = first_name[0] + last_name[:2] + year_of_birth[-2] + year_of_birth[-1]
    if username not in usernames:
        usernames.append(username)
        print("Username: {}".format(username))
        cont = input("Create another username? [Y/N] ")
        if cont == "N":
            break
    else:
        print("Username already exists.")


print("Usernames: {}".format(usernames))
