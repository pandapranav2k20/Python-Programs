# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-5
# Date:         25 SEPTEMBER 2019
'''This program uses a Leibniz sum to deirve the value of pi'''
#imported numpy in order to sum the list vals because normal sum was troubling
import numpy
#Create a list to store the values of the sum
vals = []
#Create the for loop to calculate the values of the sum
for i in range(0, int(1e4 + 1), 1):
    sol = ((-1)**i)/(2 * i + 1)
    #add the answer to the end of the list
    vals.append(sol)
#Estimate the value of pi; 4 * sum of all values in the list
pi_est = 4 * numpy.sum(vals)
#output the value of our estimate of pi
print("Pi is estimated to be:", pi_est)
'''The leibniz sum seems to be the fastest in terms of algorithm time beacuse
there is only one loop and no conditional statements'''