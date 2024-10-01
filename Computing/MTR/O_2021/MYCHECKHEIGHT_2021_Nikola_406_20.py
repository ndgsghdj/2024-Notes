number_people = int(input("Number of people: "))
minimum_age = 16
minimum_height = 1.5
names = []

for x in range(number_people):
    name = input("Name of person: ")
    age = int(input("Age of person: "))
    height = float(input("Height of person: "))

    if height >= minimum_height and age >= minimum_age:
        print("Person is tall enough and old enough.")
        names.append(name)

    elif height < minimum_height and age >= minimum_age:
        print("Person is not tall enough")
    elif age < minimum_age and height >= minimum_height:
        print("Person is not old enough.")
    else:
        print("Person is not tall enough and not old enough.")
