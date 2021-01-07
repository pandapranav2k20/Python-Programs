# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-6
# Date:         18 SEPTEMBER 2019
#
#This program checks if a user inputted string is a palindrome
#Take user input for the string
ui_orig = input("Please enter a string to be used:")
#Remove an whitespaces from the string
ui = ui_orig.replace(" ", "")
#Find the reverse of the string
stringLength = len(ui)
ui_reverse = ui[::-1]
#Determine if the string is a palindrome
if ui == ui_reverse:
    print("The string:", ui_orig, "is a plaindrome.")
else:
    print("The string:", ui_orig, "is not plaindrome.")