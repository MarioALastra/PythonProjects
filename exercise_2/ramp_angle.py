#   Calculating the Angle of the Ramp
#   Driver: Mario Lastra (U43655957) Navigator: Kalluri Deekshitha Chowdary (U22127044)

#   Importing modules
import math

#   Assigning Variables
G = 9.8
mass = int(input("Enter the mass of the cart (in kg):"))
force = int(input("Enter the force to push the cart (in N):"))

#   Calculating the angle of the ramp
angle = math.degrees( math.asin( force / (mass*G) ) )

print("The angle of the ramp is {:.1f} degrees.".format(angle))