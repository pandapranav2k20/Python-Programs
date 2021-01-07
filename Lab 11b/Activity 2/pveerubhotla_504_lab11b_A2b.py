# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-2b
# Date:         6 NOVEMBER 2019
#
'''This program creates a function that plots two arrays if they are the same
size, otherwise it returns an error message.'''
import numpy as np
import matplotlib.pyplot as plt
def plotArrays(array1, array2):
    if len(array1) == len(array2):
        plt.plot(array1, array2, '^', color = 'red', label = 'points')
        plt.xlabel('Elevation with respect to sea level (km)')
        plt.ylabel('Atmospheric Pressure (kPa)')
        plt.title('Atmospheric Pressure (kPa) vs. Elevation from sea level (km)')
        plt.legend(loc = 'upper right', frameon = True)
        plt.grid(linestyle = '-', linewidth = '0.5')
    else:
        print("Error: Arrays not the same size.")

#Test case
'''a = np.array([1654, 0, 0.1, 817, 368])
b = np.array([86.5, 101, 99.9, 92, 97.1]) 
plotArrays(a, b)'''