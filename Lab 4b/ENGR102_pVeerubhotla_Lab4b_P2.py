# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-2
# Date:         18 SEPTEMBER 2019
#
'''This program determines whether a person is underweight, healthy, overweight
or obese given their height and weight'''
#Take user input for height and weight
weight = float(input("Please enter your weight in Kilograms: "))
height = float(input("Please enter your height in meters: "))
#Calculate the BMI
def calcBMI(weight, height):
    BMI = weight / (height**2)
    return BMI
#Determine whether they are underwight, healthy, overweight, or obese
if calcBMI(weight, height) < 18.5:
    status = 'underweight'
elif 18.5 <= calcBMI(weight, height) <= 24.9:
    status = 'healthy'
elif 25.0 <= calcBMI(weight, height) <= 29.9:
    status = 'overweight'
elif calcBMI(weight, height) >= 30:
    status = 'obese'
#output their status
print("A person with height:", height, "and weight:", weight, "would be", status)