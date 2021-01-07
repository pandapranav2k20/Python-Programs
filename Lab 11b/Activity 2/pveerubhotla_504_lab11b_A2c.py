# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-2c
# Date:         6 NOVEMBER 2019
#
'''This program creates a function that finds the minimum distance from a line 
to a point.'''
import math
def calcDist(slope, intercept, point):
    a = -1 * slope
    b = 1
    c = -1 * intercept
    x = point[0]
    y = point[1]
    dist = abs(a*x + b*y + c)/math.sqrt(a**2 + b**2)
    return round(dist, 3)

#Test case
print(calcDist(1.2,2,(-3,7)))