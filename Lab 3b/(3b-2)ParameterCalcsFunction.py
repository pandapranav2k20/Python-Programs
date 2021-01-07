# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3b-2
# Date: 12 September 2019
'''This program will use a function to calculate the parameters of a 
regular polygon'''
import math
def parameter_calcs(num_sides, side_length):
        #Part A: calculate the area
        #area = (1/4) * n* s^2 * cot(pi/n)
        area_poly = (1/4) * num_sides * side_length**2 * mpmath.cot(mpmath.pi/num_sides)
        #Part B: calculate the interior angle
        #interior angle = ((n - 2) * 180)/n
        iang_poly = ((num_sides - 2) * 180)/num_sides
        #Part C: calculate the diameter of the circle inscribed in the polygon
        #inradius = (1/2) * s * cot(pi/n)
        irad_poly = (1/2) * side_length * mpmath.cot(mpmath.pi/num_sides)
        idiam_poly = irad_poly * 2
        #Part D: calculate the perimeter of the polygon
        #perimiter = n * s
        peri_poly = num_sides * side_length
        #print out all the above answers to the calculations
        print("The area of the regular polygon is: ", area_poly)
        print("The interior angle of the regular polygon is: ", iang_poly)
        print("The diameter of the circle inscribed in the regular polygon is: ", idiam_poly)
        print("The perimeter of the regular polygon is: ", peri_poly)
        print(math.tan(180/num_sides))
abcd = parameter_calcs(7, 1)