# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB2-3
# Date: 4 September 2019
#set the points
#Find the two endpoints and label them as (x1, y1) and (x2, y2) respectively.
#(1, 1) and (100, 100)
#x1 = 1
#x2 = 1
#y1 = 100
#y2 = 200
#Find the slope between the two points, the value y along the straight line is given from the equation of the slopes
#Plug that slope into the equation

x1 = 1
y1 = 1
x2 =90
y2 = 80
#prompt the user to enter an x-value between the given 1 and 100
x = float(input('Please enter a number between 1 and 100:'))
#calculates and stores the given slope
slope = (y2 - y1)/(x2 - x1)
#calculates and stores the y intercept
y_int = 1 - slope
#outputs the slope * x added t the y-intercept
print(slope * x + y_int)

