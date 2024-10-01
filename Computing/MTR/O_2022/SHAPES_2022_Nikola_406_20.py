def square_side(sq_perimeter):
    side_length = sq_perimeter / 4
    return side_length

def square_area(sq_perimeter):
    side_length = square_side(sq_perimeter)
    return side_length * side_length

def circle_diam(circumference):
    return circumference / 3.14

def circle_area(circumference):
    diameter = circle_diam(circumference)
    return 3.14 * diameter/2 * diameter/2

def output_message(shape, area):
    print("The area of the {} is {}".format(shape, area)) # Question asked for return.

while True:
    try:
        choice = input("Do you want to find: \n - The area of a square\n - The area of a circle\n").lower()
        assert choice == "square" or choice.lower() == "circle"
        break
    except:
        print("Input must be either 'square' or 'circle'.")

area = 0
if choice == 'square':
    perimeter = float(input("Perimeter of square: "))
    area = square_area(perimeter)
else:
    circumference = float(input("Circumference of circle: "))
    area = circle_area(circumference)

output_message(choice, area)
