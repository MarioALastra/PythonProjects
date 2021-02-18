#   Wind-Chill Temperature
#   Driver: Mario Lastra (U43655957) Navigator: Kalluri Deekshitha Chowdary (U22127044)

#   Assigning Variables
user_temp = int(input("Enter the temperature in Fahrenheit:"))
wind_speed = 0

#   Check input temperature
while user_temp <= -58 or user_temp >= 41:
    print("Temperature must be between -58F and 41F.")
    user_temp = int(input("Please re-enter the temperature in Fahrenheit:"))

wind_speed = int(input("Enter the wind speed miles per hour:"))

#   Check input wind speed
while wind_speed < 2:
    print("Speed must be greater than or equal to 2.")
    wind_speed = int(input("Please re-enter the wind speed miles per hour:"))

#   Calculate Wind-Chill
wind_chill = 35.74 + (0.6215 * user_temp) - ( 35.75 * (wind_speed ** 0.16) ) + (0.4275 * user_temp * (wind_speed ** 0.16))

#   Print final output
print("The wind chill index is {:.3f}".format(wind_chill))