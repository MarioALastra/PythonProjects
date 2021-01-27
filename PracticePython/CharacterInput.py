#   Character Input
#   By Mario Lastra
#   https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#   Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#   Extras:
#   Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#   Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import time
import datetime

name = input("Enter your name:")
age = int(input("Enter your age:"))

today = datetime.date.today()
future = today.year + (100-age)

print(name, " will be 100 years old in the year ", future, ".", sep='')

repeat = int(input("Give me a number:"))

for x in range(repeat):
    print(name, " will be 100 years old in the year ", future, ".", sep='')