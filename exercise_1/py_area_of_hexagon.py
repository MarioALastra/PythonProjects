#   Area of a Hexagon
#   Driver: Mario Lastra U43655957  Navigator: Collin Reynolds U78898749

import math

#   Get user input
side_length = float(input("Enter the side length of the hexagon:"))

#   Calculate the area
area = ( (3*math.sqrt(3)) / 2) * math.pow(side_length, 2)

print("The area of a hexagon with side length", side_length, "is", '{:.3f}'.format(area))