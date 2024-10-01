# num_students = 10
colours = []
while True:
    colour = input("What is the student's favourite colour? ")
    colour = colour.lower()

    colours += [colour]

    cont = input("Do you want to enter another colour? [Y/N] ")
    if cont.upper() == "Y":
        continue
    else:
        break

search_colour = input("Enter a colour to search for: ").lower()
students = 0

for colour in colours:
    if colour == search_colour:
        students += 1

print("Colour: {}".format(search_colour))
print("Number of students who have {} as a favourite colour: {}".format(search_colour, students))
