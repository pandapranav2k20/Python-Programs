# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-2
# Date:         30 SEPTEMBER 2019
#
'''This program finds all the Armstrong numbers between 0 and 199'''
#Create a blank list to store the Armstrong numbers
armstrongs = []
#Create a loop for values of 0 to 999 to find the Armstrong numbers
for i in range(0, 1000):
    #If i is a single digit number
    if i < 10:
        if i**3 == 1:
            armstrongs.append(i)
    #If i is a double digit number
    elif i < 99:
        #Seperate i into digits
        str_i = str(i)
        i_dig1 = int(str_i[0])
        i_dig2 = int(str_i[1])
        if (i_dig1**3 + i_dig2**3) == i:
            armstrongs.append(i)
    #If i is a triple digit number
    elif 100 <i <= 999:
        str_i = str(i)
        #Seperate i into digits
        i_dig1 = int(str_i[0])
        i_dig2 = int(str_i[1])
        i_dig3 = int(str_i[2])
        if(i_dig1**3 + i_dig2**3 + i_dig3**3) == i:
            armstrongs.append(i)
            
#Output the list of Armstrong numbers
print("The list of Armstrong numbers between 0 and 999 is as follows:", armstrongs)