# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-4
# Date:         25 SEPTEMBER 2019
'''This program uses the monte carlo approach to estimate the value of pi'''
import random 
import math
#Create the variables to store the current and previous estimates
current_est = 1
previous_est = 0
#Create the variable to store the number of iterations
num_iterations = 0
#Create variables to store the numbers of points
points_inside = 0
total_points = 0
#Create the while loop to estimate pi
while abs(current_est - previous_est) >= 1e-4 or (current_est == 4 and previous_est == 4):
    num_iterations +=1
    previous_est = current_est
    #Create the variabls x and y as random values between 0 and 1
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        points_inside += 1
        total_points += 1
    else:
        total_points += 1
    #estimate thevalue of pi given the total number of points and points insde
    current_est = 4 * (points_inside/total_points)
#Set the current estimate equal to final estimate
final_est = current_est
#Print the final estimate for pi and the number of iterations
print("The value of pi is estimated to be:", final_est)
print("The estimate took", num_iterations, "iterations.")
'''The monte carlo apporach always seems to hover around the 8000 iteration mark,
while the other approach needs less iterations'