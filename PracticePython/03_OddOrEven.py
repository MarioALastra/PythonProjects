#   Odd or Even
#   By Mario Lastra
#   https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

#   Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#   Hint: how does an even / odd number react differently when divided by 2?
#   Extras:
#   If the number is a multiple of 4, print out a different message.
#   Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

user_number = int(input("Enter a number:"))

is_even = (user_number % 2 == 0)
is_mult_of_four = (user_number % 4 == 0)

if is_even and not is_mult_of_four:
    print("{0:d} is an even number!".format(user_number))
elif is_even and is_mult_of_four:
    print("{0:d} is a multiple of 4!".format(user_number))
else:
    print("{0:d} is an odd number!".format(user_number))

user_number = int(input("Enter a number:"))
user_divide = int(input("Enter a number to divide by:"))

if user_number % user_divide == 0:
    print("{1:d} divides evenly into {0:d}!".format(user_number, user_divide))
else:
    print("{1:d} does not divide evenly into {0:d}!".format(user_number, user_divide))