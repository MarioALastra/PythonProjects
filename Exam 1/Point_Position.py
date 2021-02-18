#   Point Position
#   Mario Lastra (U43655957)
#   This script determines whether a point is on the left of the line, 
#   on the right of the line, or on the line itself.

p0_x = float(input("Enter the x-coordinate for point p0:"))
p0_y = float(input("Enter the y-coordinate for point p0:"))
p1_x = float(input("Enter the x-coordinate for point p1:"))
p1_y = float(input("Enter the y-coordinate for point p1:"))
p2_x = float(input("Enter the x-coordinate for point p2:"))
p2_y = float(input("Enter the y-coordinate for point p2:"))

#   Calculate Conditions
left_of_line = ( (p1_x - p0_y) * (p2_y - p0_y) - (p2_x - p0_x) * (p1_y - p0_y) ) > 0
right_of_line = ( (p1_x - p0_y) * (p2_y - p0_y) - (p2_x - p0_x) * (p1_y - p0_y) ) < 0

#   Determine Output
if left_of_line:
    print("p2 at coordinates ( {0} , {1} ) is on the left side of the line\nfrom point ( {2} , {3} ) to point ( {4} , {5} )".format(p2_x, p2_y, p0_x, p0_y, p1_x, p1_y))
elif right_of_line:
    print("p2 at coordinates ( {0} , {1} ) is on the right side of the line\nfrom point ( {2} , {3} ) to point ( {4} , {5} )".format(p2_x, p2_y, p0_x, p0_y, p1_x, p1_y))
else:
    print("p2 at coordinates ( {0} , {1} ) is on the line\nfrom point ( {2} , {3} ) to point ( {4} , {5} )".format(p2_x, p2_y, p0_x, p0_y, p1_x, p1_y))

