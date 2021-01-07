# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-4
# Date:         18 SEPTEMBER 2019
#
'''This program calculates real and imaginary roots for quadric functions given
the coefficients for a, b, and c'''
import cmath
import math
#Take the user input for the three values for a, b, and c
a = float(input("Please enter the value of the coefficent a:"))
b = float(input("Please enter the value of the coefficent b:"))
c = float(input("Please enter the value of the coefficent c:"))
#Find and store the value of the discriminant
disc = b**2 - 4 * a * c
#Calculate the roots using if statements and the discriminant
#Helped by David Hernandez(502) with the logic behind the below conditionals
if disc > 0:
    sol1 = (-b - math.sqrt(disc)) / (2 * a)
    sol2 = (-b + math.sqrt(disc)) / (2 * a)
    print("The roots are:", sol1, ",", sol2)
elif disc == 0:
    sol1 = (-b + math.sqrt(disc)) / (2 * a)
    print("The roots are:", sol1)
elif a == 0 and b == 0 and c == 0:
    print("There are an infinite number of solutions")
elif disc < 0:
    #If the discriminant is less than zero we will have imaginary roots
    sol1 = (-b - cmath.sqrt(disc)) / (2 * a)
    sol2 = (-b + cmath.sqrt(disc)) / (2 * a)
    print("There are no real solutions.","The complex roots are:", sol1, ",", sol2)