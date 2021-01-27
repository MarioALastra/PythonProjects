#   List Less Than Ten
#   By Mario Lastra
#   https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

#   Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
#   Extras:
#   Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#   Write this in one line of Python.
#   Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b_list = []
c_list = []
d_list = []

#   Long way
for x in a_list:
    if x < 5:
        b_list.append(x)

#   Short Way
c_list = [x for x in a_list if x < 5]

print("B List:", b_list)
print("C List:", c_list)

user_number = int(input("Enter a number:"))
d_list = [x for x in a_list if x < user_number]

print("D List:", d_list)