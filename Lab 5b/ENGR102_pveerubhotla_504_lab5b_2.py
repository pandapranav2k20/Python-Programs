# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-2
# Date:         25 SEPTEMBER 2019
'''This program takes in an undefined amount of measurements in and calculates
the average, minimum, and maximum'''
#Create a list to store the measurements inputted by the user
measurements = []
#Create a variable to store the current measurements
current_measurement = 0
#Take in the user input to fill the list with measurements
while current_measurement >= 0:
    #Take the user input for the new measurement
    new_measurement = float(input("Please enter the measurement:"))
    #If the measurement is non-negative, add it to the list
    if new_measurement >= 0:
        measurements.append(new_measurement)
    #If the new measurement is less than zero, exit the while loop
    else:
        current_measurement = new_measurement
        
#Calculate the average of the measurements
sum = 0
#Use a for loop in range(measurements) to find the average
for i in measurements:
    sum += i
#Divide the sum by the number of terms
average = sum/len(measurements)
#Ourput the average of the measurements
print("The average of the measurements is:", average)

#Calculate the maximum of the measurements
#Create the variable to store the current maximum
current_max = measurements[0]
#Use a for loop using i in measuremnts to find the maximum
for i in measurements:
    #If i is greater than the current maximum, set current_max = i
    if i > current_max:
        current_max = i
#Output the maximum measurement
print("The maximum measurement is:", current_max)

#Calculate the minimum of the measurements
#Create the variable to store the current minimum
current_min = measurements[0]
#Use a for loop using i in measuremnts to find the minimum
for i in measurements:
    #If i is less than the current minimum, set current_min = i
    if i < current_min:
        current_min = i
#Output the minimum measurement
print("The minimum measurement is:", current_min)