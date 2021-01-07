# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Benson Nguyen
#               Pranav Veerubhotla
#               Jolie Hand
#               Emily Hotz
# Section:      504
# Assignment:  Lab3
# Date:         11 Sep 2019
# Goal: convert inputted BTUs into outputted Joules
# Ask user for input of BTUs
BTU = input("How many BTUs? ")
# Convert input into a float
BTU = float(BTU) # unit: BTUs
# Convert float into Joules
Joule = BTU * 1055.0559 # unit: Joules
# Output # of Joules
print("That is equal to",Joule,"Joules.")