first_name = input("First name: ")
last_name = input("Last name: ")
year_of_birth = input("Year of birth: ")

username = first_name[0] + last_name[:2] + year_of_birth[-2] + year_of_birth[-1]

print("Username: {}".format(username))
