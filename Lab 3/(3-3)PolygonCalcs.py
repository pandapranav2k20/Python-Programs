# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3-3
# Date: 11 September 2019
import math
#Formulas needed for this program
#For formulas: r = circumradius, n = number of sides
#Perimeter = 2 * n * r * sin(pi/n)
#Apothem = r * cos(180/n)
#Area = (r**2 * n * sin(360/n))/2

#Take the user input for the circumradius and num of sides
num_sides = int(input("Please enter the number of sides: "))
cir_rad = float(input("Please enter the circumradius: "))

#Calculate and store the calculations for Apothem, Area, and Perimeter
def calc_parameters(num_sides, cir_rad):
        perimeter = 2 * num_sides * cir_rad *math.sin(math.pi/num_sides)
        apothem = cir_rad * math.cos(math.pi/num_sides)
        area = (cir_rad**2 * num_sides * math.sin((2 * math.pi)/num_sides))/2
        #Build a tuple using the calculations above
        calc_tuple = (perimeter, apothem, area)
        return calc_tuple
#print the tuple
print("Calculations output in perimeter, apothem, area with expected units")
print(calc_parameters(num_sides, cir_rad))