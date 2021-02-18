#   String List
#   By Mario Lastra
#   https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

#   Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

user_input = input("Enter a word:")
reversed_input = user_input[::-1]

if user_input.lower() == reversed_input.lower(): 
    print("{} is a palindrome!".format(user_input))
else: 
    print("{} is a not palindrome!".format(user_input))