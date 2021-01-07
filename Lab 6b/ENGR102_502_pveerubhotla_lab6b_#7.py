# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-7
# Date:         30 SEPTEMBER 2019
#
'''This Program prints a list with a string indicating whether the integer 
following it is even or odd, then the integer'''
#Create blank lists for strings, integers, and the final combined list
str_list = []
int_list = []
fin_list = []

#Create the lsit to hold the strings(even or odd)
for i in range(21):
    if i % 2 == 0:
        str_list.append("even")
    else:
        str_list.append("odd")

#Create a list to hold the integers(0 to 20)
for j in range(21):
    int_list.append(j)

#Apeend the string value and integer at index k from their respective lists to the final lsit    
for k in range(21):
    comb_elem = [str_list[k], int_list[k]]
    fin_list.append(comb_elem)

#Output the final list
print("The final list is:", fin_list)