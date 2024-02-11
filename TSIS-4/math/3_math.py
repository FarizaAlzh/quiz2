# Write a Python program to calculate the area of regular polygon.
import math
sides = 4
length_side = 25
# Area = (number of sides × length of one side × apothem)/2.
apothem = length_side /(2*math.tan(math.pi/sides))
area_polygon = (sides * length_side * apothem)/2
print(int(area_polygon))


# area of the polygon is: 625