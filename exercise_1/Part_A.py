#program for calculating slope of a line
#driver: Collin Reynolds (U78898749) navigator: Mario Lastra (U43655957)

#assigning coordinates as variables
x1 = float(input('Enter the x-coordinate for Point 1:'))
y1 = float(input('Enter the y-coordinate for Point 1:'))
x2 = float(input('Enter the x-coordinate for Point 2:'))
y2 = float(input('Enter the y-coordinate for Point 2:'))

#assigning slope to expression
slope = (y2 - y1) / (x2 - x1)

#returning output
print("The slope for the line that connects two points (", x1, ",", y1, ") and (", x2, ",", y2, ") is", '{:.5f}'.format(slope))
