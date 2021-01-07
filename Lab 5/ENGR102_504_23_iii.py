# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Damon Tran
#               Benson Nguyen
#               Matt Knauth
#               Pranav Veerubhotla
# Section:      504
# Assignment:   lab 5-1 III
# Date:         23 Sept 2019
'''This program takes user input for side lengths of triangles and determines
whether the triangle is equilateral, isoceles, scalene, or ill-formed. The 
program will continue to run until the user enters 'stop'.'''
#Initialize a variable to hold the user input
user_input = ''
#Create an empty list to store the side lengths of the triangles
sidelengths = []
#Create an empty variable to store the type of triangle
triangle = ''
while user_input != 'stop':
    #Fill the list lengths with the three side lengths of the trianlge
    while len(sidelengths) < 4:
        user_input = (input("Please enter side legnth:"))
        #If the user enters stop break the loop
        if user_input == 'stop':
            break
        #Otherwise convert the user input from Str to float
        else:
            user_input = float(user_input)
        sidelengths.append(user_input)
    #Determine whether the triangle is ill-formed, equilateral, or scalene
    if sidelengths[0] == sidelengths[1] and sidelengths[0] == sidelengths[2]:
        triangle = 'equilateral'
    elif sidelengths[0] == sidelengths[1] or sidelengths[0] == sidelengths[2]:
        triangle = 'isoceles'
    #Determine if the triangle ill formed, if it is not it must be scalene
    elif ((sidelengths[0] + sidelengths[1]) > sidelengths[2] and (sidelengths[0] + sidelengths[2]) > sidelengths[1]) and (sidelengths[1] + sidelengths[2]) > sidelengths[0]:
        triangle = 'scalene'
    else:
        triangle = 'ill-formed'
    #Output the type of triangle
    print("The triangle is:", triangle)