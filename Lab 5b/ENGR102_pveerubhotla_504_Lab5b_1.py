# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-1
# Date:         25 SEPTEMBER 2019
'''This program creates a collatz sequence starting with an integer inputted by
the user'''
#Take in user input for the starting value of the Collatz Sequence
start = int(input("Please enter the enteger for which the series will begin with:"))
#Create a list to store the values of the sequence
vals = [float(start)]
#Create a variable to store the current value of the series
current_val = 0
#Create a loop that executes if the final value of the series is not 1
while current_val != 1:
    if (start%2) == 0:
        current_val = start/2
        start = current_val
    elif (start%2) == 1:
        current_val = 3 * start + 1
        start = current_val
    vals.append(current_val)
#If current_val = 1, then the series is finished and it is time to output the series
if current_val == 1:
    print("The Collatz sequence is:",vals)