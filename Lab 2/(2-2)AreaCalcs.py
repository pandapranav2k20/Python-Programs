# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB2-2
# Date: 4 September 2019

#program calculates area of Geometric shape
from math import *
#define variables for various area calculations below
length_r1 = 16 #units
width_r1 = 12 #units
#the rectangles have the same dimensions for length and width, therefore we do not need to create seperate vars for rect2
base_tri = 16 #units
height_tri = 12 #units
#using the two legs of the triangle, use Pythag theorem to calculate the length of the Hypotenuse
hypotenuse_tri = sqrt(base_tri**2 + height_tri**2) #units
#radius of the circle is equal to 1/2 of the hypotenuse of the triangle
radius_sc = hypotenuse_tri/2 #units

#break up shape/calc area for several pieces
#2 12' x 16' rectangles
#multiply calculation by two, because we have two rectangles with r1's dimensions
area_r1r2 = 2 * length_r1 * width_r1 #units squared
#1 12' x 16' triangle
area_tri = base_tri * height_tri * (1/2) #units squared
#1 semicircle with diameter = sqrt(12**2 + 16**2)
area_sc = pi * radius_sc**2 * (1/2) #units squared

#add all the areas together
area_total = area_r1r2 + area_tri + area_sc #units squared
#print the sum of the areas
print('The area of the shape is:', area_total, 'units squared')