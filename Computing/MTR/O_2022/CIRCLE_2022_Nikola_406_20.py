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

