# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-3
# Date:         25 SEPTEMBER 2019
'''This program uses the logic from lab 3b combined with loops to estimate
the value of pi to a percision of 1e-4'''
import math
#Create variables for the current estimate and previous estimate
current_est = 1
previous_est = 0
#Create the variables for the number of sides and number of iterations.
num_sides = 2
cir_d = 1
num_iterations = 0
#Create the while loop where the number of sides of the polygon are increased each iteration
while (abs(current_est - previous_est) >=  1e-4) or abs(current_est - math.pi >= 1e-4):
    num_sides += 1
    num_iterations += 1
    previous_est = current_est
    #Insert the function used to estimate pi
    def calc_pi(num_sides): 
        #find the angle needed for the calculations
        angle = ((360 / (2 * num_sides)) * (math.pi / 180))  
        #use the angle to find the inscribed perimeter
        peri_ins = 2 * num_sides * (1/2) * math.sin(angle)
        #find the second angle needed for the calculations
        angle_2 = ((360 / (2 * num_sides)) * (math.pi / 180))
        #use the second angle to find the circumscribed perimeter
        peri_circ = 2 * num_sides * (1/2) * math.tan(angle_2)
        #calculate the average of the inscribed and circumscribed perimeters
        avg_perimeter = (peri_ins + peri_circ) / 2
        pi_est = avg_perimeter/cir_d
        return pi_est
    current_est= calc_pi(num_sides)
#Output the estimate of pi and the number of iterations
print("The estimate for pi is:", current_est)
print("The estimate took", num_iterations, "iterations.")
