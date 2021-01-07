# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Damon Tran
#               Benson Nguyen
#               Matt Knauth
#               Pranav Veerubhotla
# Section:      504
# Assignment:   lab 5-1(iv)
# Date:         23 Sept 2019
'''This program calculates the sine of an angle which the user inputs(in degrees)
using the Maclarurin series with a user number supplied of terms'''
import math
#Take the user input for the angle(in degrees)
angle = float(input("Please enter the angle in degrees:"))
#Take the user input for the number of terms
num_terms = int(input("Please enter the number of terms:"))

#Create a list to store the solutions for the sum formula
sols = []
#Calculate the sine of the angle using the Maclarurin series using loops
#We will use a loop to sum the values, and each iteration write the value into a list
for i in range(num_terms):
    #iterable = ((-1**n)/((2n+1)!)) * anlge**(2n + 1)
    latest_sol = ((-1**i)/(math.factorial(2 * i + 1))) * (angle*math.pi/180)**(2 * i + 1)
    #We will need to store the abs() of the values of the sum from n = 0 to n = numebr of terms -1
    sols.append(abs(latest_sol))
#After writing the values of the sum into a list, we will use the sum() function to sum the list
#Maclarurin series = sum(list)
angle_sine = sum(sols)
#Maclarurin series = sum(list)
#Output the sum calculated above as the sine of the angle the user inputted
print(angle_sine)