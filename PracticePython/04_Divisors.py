#   Divisors
#   By Mario Lastra
#   https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

#   Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#   (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#   For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

user_number = int(input("Enter a number:"))

divisior_list = range(2, 101)

current_divisior = [elements for elements in divisior_list if user_number % elements == 0]

print(current_divisior)