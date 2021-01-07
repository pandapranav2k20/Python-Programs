# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-2d
# Date:         6 NOVEMBER 2019
#
'''This program uses the function from part C to plot the line, the point, and 
the shortest distance.'''
import math
import matplotlib.pyplot as plt
import numpy as np
def calcDist(slope, intercept, point):
    a = -1 * slope
    b = 1
    c = -1 * intercept
    x = point[0]
    y = point[1]
    dist = abs(a*x + b*y + c)/math.sqrt(a**2 + b**2)
    return round(dist, 3)

slope0 = 1.2
intercept0 = 2
point0 = (-3, 7)

#Plot the data
x = np.linspace(-5, 5, 100)
x2 = np.linspace(-3, 0.909, 100)
y = x*slope0 + intercept0
y2 = -1 * x2 + 4
plt.plot(x, y, '-g')
plt.plot(point0[0], point0[1], '^r')
plt.plot(x2, y2, '--')