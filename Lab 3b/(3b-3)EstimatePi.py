# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3b-3
# Date: 12 September 2019
import math
'''This program estimates the value of pi using a method outlined by Archimedes'''
cir_d = 1 #We are instructed to use 1 as the value for D
#Take the user's input for the number of sides for both polygons
ui_num_sides = int(input("Please enter the number of sides for both polygons: "))
#Use function to calculate perimeter
def calc_perimeter(ui_num_sides): #David Hernandez(ENGR102-502) helped me with this function
        #find the angle needed for the calculations
        angle = ((360 / (2 * ui_num_sides)) * (math.pi / 180))  
        #use the angle to find the inscribed perimeter
        peri_ins = 2 * ui_num_sides * (1/2) * math.sin(angle)
        #find the second angle needed for the calculations
        angle_2 = ((360 / (2 * ui_num_sides)) * (math.pi / 180))
        #use the second angle to find the circumscribed perimeter
        peri_circ = 2 * ui_num_sides * (1/2) * math.tan(angle_2)
        #calculate the average of the inscribed and circumscribed perimeters
        avg_perimeter = (peri_ins + peri_circ) / 2
        return avg_perimeter
#calculate the supposed value of "pi"
pi_obs = calc_perimeter(ui_num_sides)/cir_d
#output the supposed value of "pi"
print("The value of pi is proven to be: ", pi_obs)
accuracy = abs((math.pi - pi_obs) / math.pi * 100)
print("The accuracy with", ui_num_sides, "is:", accuracy, "%")

'''In order for the accuracy to be less than 1% of the total value there must 
be at least 10 sides'''

'''In order for the accuracy to be less than 0.1% of the total value there must
be at least 91 sides'''

'''The value of pi in python has 16 significant figures, because it is a float 
and floats only have 64 bis worth of space in python.'''