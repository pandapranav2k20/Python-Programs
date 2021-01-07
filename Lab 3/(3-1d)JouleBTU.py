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
# Goal: convert inputted Joules into outputted BTUs
# Ask user for input of Joules
Joule = input("How many Joules? ")
# Convert input into a float
Joule = float(Joule) # unit: Joules
# Convert float into BTUs
BTU = Joule / 1055.0559 # unit: BTUs
# Output # of BTUs
print("That is equal to",BTU,"BTUs.")


