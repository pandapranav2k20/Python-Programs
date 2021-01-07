# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-4
# Date:         18 SEPTEMBER 2019
#
#This program calculates the number of widgets given the number of days
import math
#Take in user input for the number of days
numdays  = int(input("Please enter the number of days: "))
#Calculate the number of widgets given the number of days
if numdays <= 10:
    num_widgets = 10 * numdays
elif 11 <= numdays <= 60:
    num_widgets = 10 * 10 + 40 * (numdays - 10)
elif numdays <= 99:
    num_widgets = 10 * 10 + 40 * 39 + 39 * (numdays - 49)
elif 61 <= numdays <= 100: #Helped by David Hernandez(502) with this elif statement
    #Sum formula is n(n-1)/2
    Sum = 40 - (numdays - 60)
    num_widgets += int(2100 + ((39*40)/2 - (Sum - 1) * Sum/2))
#Output the number of widgets
print("There are", num_widgets, "widgets after", numdays, "days.")
