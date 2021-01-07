# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Damon Tran
#               Benson Nguyen
#               Matt Knauth
#               Pranav Veerubhotla
# Section:      504
# Assignment:   lab 5-2
# Date:         23 Sept 2019
'''This program uses a binary search in order to find the roots of a cubic 
function with coefficients a, b, c, and d'''
import math
#Take in the user input for the coefficients:
A = float(input("Please enter the value for the coeffcient a:"))
B = float(input("Please enter the value for the coeffcient b:"))
C = float(input("Please enter the value for the coeffcient c:"))
D = float(input("Please enter the value for the coeffcient d:"))
#Take in the user input for the bounds:
bound_low = float(input("Please enter the lower bound:"))
bound_high = float(input("Please enter the upper bound:"))

#Calculate the values of the slope of thecubic function at the lower and upper bounds
slope_lower = 3 * A*bound_low**2 + 2 * B*bound_low**1 + C
slope_upper = 3 * A*bound_high**2 + 2 * B*bound_high**1 + C
#Calculate the values at the lower and upper bounds
interval = bound_high - bound_low
while interval > 10**(-6):
    value_lower = (A *((bound_low)**3)) + (B *((bound_low)**2)) + (C * bound_low) + D
    value_upper = (A *((bound_high)**3)) + (B *((bound_high)**2)) + (C * bound_high) + D
    if (value_lower < 0 or value_upper < 0) and (value_lower > 0 or value_upper > 0):
        p = (bound_low + bound_high) / 2
        #Calculate f(p)
        value_p = A *p**3 + B *p**2 + C *p**1 + D
        #Determine whether f(p) is negative, positive, or the solution
        if value_p == 0:
            finalSolution = p
        elif value_p < 0:
            bound_low = p
        elif value_p > 0:
            bound_high = p
        interval = bound_high - bound_low
        
print(finalSolution)