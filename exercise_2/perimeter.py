#Perimeter of a triangle
#Driver: Kalluri Deekshitha Chowdary(U22127044), Navigator: Mario Lastra(U43655957)

#Assigning Variables
a= float(input("Enter length of edge1:"))
b= float(input("Enter length of edge2:"))
c= float(input("Enter length of edge3:"))

#formula to find perimeter of a triangle
perimeter = a+b+c

#Checking the validity of the perimeter
if (a+b>c) and (b+c>a) and (c+a>b):
    print("The perimeter is:", perimeter)

else:
     print("Perimeter cannot be calculated: the input is invalid ")
