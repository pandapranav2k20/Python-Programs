# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-1
# Date:         18 SEPTEMBER 2019
#
'''This program takes user input for 3 numebrs then uses if statements to 
output the largest number'''
#Take the user input for the three numbers
num1 = float(input("Please enetr the first number:"))
num2 = float(input("Please enetr the second number:"))
num3 = float(input("Please enetr the third number:"))
if num3 > num2 and num3 > num1:
    print(num3, ",Num 3 is the greatest number")
if num2 > num3 and num2 > num1:
    print(num2, ", Num 2 is the greatest number")
if num1 > num2 and num1 > num3:
    print(num1, ", Num 1 is the greatest number")