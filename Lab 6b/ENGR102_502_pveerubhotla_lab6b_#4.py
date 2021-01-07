# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-4
# Date:         30 SEPTEMBER 2019
#
'''This program takes in positive integers and creates two lists, one of all 
the integers and one of the even ones'''
'''For some reason in the directions, they say to name the list of even integers
List1_odd, I know this is wrong but I'm just following the directions'''
#Take the user input for the first integer
ui = int(input("Plese enter a positive integer:"))
#Create the blank lists that will be filled with pos. integers and even-pos. integers
List1_all = []
List1_odd = []
#Create a loop that continues taking values as long as the user does not input -1
while ui != -1:
    #If the user enters a pos. value
    if ui > 0:
        print("Excellent!")
        #Add the posiitive integer to the list
        List1_all.append(ui)
        ui = int(input("Please enter a positive integer:"))
    #If the user enters a 0 or a neg. value other than -1
    elif ui == 0 or ui < -1:
        ui = int(input("Please enter a positive value:"))

#Use a loop to isolate the even values in the all list, add them to the oddList
for i in List1_all:
    if i % 2 == 0:
        List1_odd.append(i)

#Output each list if they are not empty   
if len(List1_all) > 0:
    print("The list of all the numbers entered is:", List1_all)

if len(List1_odd) > 0:
    print("The list of even numbers entered is:", List1_odd)
