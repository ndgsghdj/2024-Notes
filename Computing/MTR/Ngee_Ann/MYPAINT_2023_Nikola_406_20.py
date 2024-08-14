# Task 1 #

print("Welcome to ColorBest Painting Services!")

apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room: ")

if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5

paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free (C)Premier all-in-one: ")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
elif paint_type == "C":
    base_cost = 2200

total_cost = base_cost + 120*no_rooms

colour_type = []

print("Colours selected are:")

j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1

for i in range(1,no_rooms+1):
    while True:
        try:
            colour_code = input("Select paint color(01 to 58) for Room {}: ".format(i))
            assert int(colour_code) >= 1 and int(colour_code) <= 58
            break
        except:
            print("Colour code must be an integer between 1 and 58 inclusive.")

    colour_type += [colour_code]

print("Total package price: {}".format(total_cost))
