#   Fizz Buzz
#   By Mario Lastra

fizzBuzzList = []

def FizzBuzz(number):
    #   Create a list that stores input, fizz, buzz, and fizzbuzz. 
    fb_list = [number, "Fizz", "Buzz", "FizzBuzz"]

    fizz = (number % 3 == 0)     #   If fizz is true, fizz = 1
    buzz = (number % 5 == 0) * 2 #   If buzz is true, buzz = 2

    #   Get a value from the list at index fizz+buzz. Ex: fizz+buzz = 0 Return input | fizz+buzz = 3 Return "FizzBuzz"
    return fb_list[fizz+buzz]

#   Loop from 1 to 100 and calculate FizzBuzz
for x in range(1,101):
    fizzBuzzList.append(FizzBuzz(x))

#   Print list
print(fizzBuzzList)
