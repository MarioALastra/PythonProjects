#   Runway Length
#   Driver: Mario Lastra U43655957  Navigator: Collin Reynolds U78898749

#   Assigning variables
v = float(input("Enter the plane's take off speed in m/s: "))
a = float(input("Enter the plane's acceleration in m/s^2: "))

#   Calulating Minimum length
length = (v**2) / (2*a)

y = format(103/4, '.1f')

#   Print Output
print("The minimum runway length needed for this airplane is", '{:.4f}'.format(length), "meters.")