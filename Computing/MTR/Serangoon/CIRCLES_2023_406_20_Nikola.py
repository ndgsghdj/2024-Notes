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

