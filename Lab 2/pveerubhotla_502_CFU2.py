# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: CFU2
# Date: 4 September 2019
from math import *
#calculate what is defined in the directions of CFU2

#calculate and output the area and perimeter of a circle with radius 3.21 units
#define the radius
radius_cir = 3.21 #units
#calculate the area of the circle
area_cir = pi * radius_cir**2 #units squared
#calculate the perimeter of the cicrle
perimeter_cir = 2 * pi * radius_cir #units
#output the respective area and perimeter
print('The area of the circle is:', area_cir,'units squared.','The perimeter of the circle is:', perimeter_cir, 'units')

#calculate and output the length of the side of square that has the same area as the circle
#calculate length of square side
#side + sqaure root (area of the circle)
side_sq1 = sqrt(area_cir) #units
#output the length of the side(units) of the square that has the same area as the circle
print('The length of the side of the square that has the same area as the circle is:', side_sq1, 'units')

#calculate and output the legth of the side of the square that has the same perimeter as the circle
#calculate length of side of square
#side = perimeter of cirlce / 4
side_sq2 = perimeter_cir/4 #units
#output the length of the side(units) of the square that has the same perimeter as the circle
print('The length of the side of the square that has the same perimeter as the circle is:', side_sq2, 'units')