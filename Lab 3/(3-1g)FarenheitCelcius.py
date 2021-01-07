# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3-1g
# Date: 9 September 2019
#convert from Farenheit to Celcius
import math
#take the users input for the temprature
temp_f = int(input("Please enter the Temperature in Farenheit: "))
#convert from Farenheit to Celcius
temp_c = (temp_f - 32) * (5/9)
#output the Temperature in degrees celcius
print("The temperature in Ceclius is: ", temp_c, "degrees")