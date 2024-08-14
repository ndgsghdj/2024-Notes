import math

def area_circle(radius):
    area = 3.142 * radius**2
    return area

def volume_cone(radius, vertical_height):
    volume = (1/3) * area_circle(radius) * vertical_height
    return volume

def slant_height(radius, vertical_height):
    slant_height = math.sqrt(pow(radius, 2) + pow(vertical_height, 2))
    return slant_height

def surface_area_cone(radius, vertical_height):
    total_surface_area = area_circle(radius) + 3.142 * slant_height(radius, vertical_height)
    return total_surface_area

while True:
    try:
        choice = int(input("Do you want to find:\n(1) Area of a circle\n(2) Volume of a cone\n(3) Total surface area of a cone\nChoice: "))
        assert choice in [1,2,3]
        break
    except:
        print("Your choice must be either 1, 2, or 3.")

radius = float(input("Radius: "))

if choice == 1:
    print("The area of circle is {:.2f}".format(area_circle(radius)))
elif choice == 2 or choice == 3:
    vertical_height = float(input("Vertical height of cone: "))
    if choice == 2:
        print("The volume of cone is {:.2f}".format(volume_cone(radius, vertical_height)))
    elif choice == 3:
        print("The surface area of cone is {:.2f}".format(surface_area_cone(radius, vertical_height)))
