# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB2b-2c
# Date: 7 September 2019
from math import *
#this program does 3D Linear Interpolation
#point 1, assume all distances in meters and all times in seconds
x1 = 1
y1 = 3
z1 = 7
time1 = 13
#point 2
x2 = 23
y2 = -5
z2 = 10
time2 = 84
#time we want to find the 3rd point at
targetTime1 = 20
targetTime2 = 27.5
targetTime3 = 35
targetTime4 = 42.5
targetTime5 = 50
#create an equation to solve for x3
slope_x = (x2 - x1)/(time2 - time1)
constant_x = x2 - slope_x * time2
equation_x = slope_x * targetTime1 + constant_x

#create an equation to solve for y3
slope_y = (y2 - y1)/(time2 - time1)
constant_y = y2 - slope_y * time2
equation_y = slope_y * targetTime1 + constant_y

#create an equation to solve for z3
slope_z = (z2 - z1)/(time2 - time1)
constant_z = z2 - slope_z * time2
equation_z = slope_z * targetTime1 + constant_z

#all the equation variables calculate the exact points for x3, y3, and z3 at t = 20
#output the points from above
print("The location of x at time = 20 seconds is: ", equation_x)
print("The location of y at time = 20 seconds is: ", equation_y)
print("The location of z at time = 20 seconds is: ", equation_z)
print("--------------------------------------------------------------")

#reset the equations to use the next target time
equation_x = slope_x * targetTime2 + constant_x
equation_y = slope_y * targetTime2 + constant_y
equation_z = slope_z * targetTime2 + constant_z

#output the points for t = 27.5
print("The location of x at time = 27.5 seconds is: ", equation_x)
print("The location of y at time = 27.5 seconds is: ", equation_y)
print("The location of z at time = 27.5 seconds is: ", equation_z)
print("--------------------------------------------------------------")

#reset the equations to use the next target time
equation_x = slope_x * targetTime3 + constant_x
equation_y = slope_y * targetTime3 + constant_y
equation_z = slope_z * targetTime3 + constant_z

#output the points for t = 35
print("The location of x at time = 35 seconds is: ", equation_x)
print("The location of y at time = 35 seconds is: ", equation_y)
print("The location of z at time = 35 seconds is: ", equation_z)
print("--------------------------------------------------------------")

#reset the equations to use the next target time
equation_x = slope_x * targetTime4 + constant_x
equation_y = slope_y * targetTime4 + constant_y
equation_z = slope_z * targetTime4 + constant_z

#output the points for t = 42.5
print("The location of x at time = 42.5 seconds is: ", equation_x)
print("The location of y at time = 42.5 seconds is: ", equation_y)
print("The location of z at time = 42.5 seconds is: ", equation_z)
print("--------------------------------------------------------------")

#reset the equations to use the next target time
equation_x = slope_x * targetTime5 + constant_x
equation_y = slope_y * targetTime5 + constant_y
equation_z = slope_z * targetTime5 + constant_z

#output the points for t = 50
print("The location of x at time = 50 seconds is: ", equation_x)
print("The location of y at time = 50 seconds is: ", equation_y)
print("The location of z at time = 50 seconds is: ", equation_z)


