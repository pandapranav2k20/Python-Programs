# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 5b-5
# Date:         25 SEPTEMBER 2019
'''This program uses the Russian Peasant method to carry out long multiplication'''
#Take the user input for the two numbers being multiplied
ui_1  = int(input("Please enter the first number to be mutiplied:"))
ui_2  = int(input("Please enter the second number to be mutiplied:"))
#Add the user inputs to their respective lists
#Create two lists to represent the two columns
col1 = [ui_1]
col2 = [ui_2]
i = 0
#Create the while loop to calculate column one
while col1[i] != 1:
    col1.append(int(col1[i]/2))
    i += 1
#Create the list to calculate column two
j = 0
while len(col2) < len(col1):
    col2.append(int(col2[j] * 2))
    j += 1
#Store the current length of column 1
length_col1 = len(col1)
#Cross out the rows with an even number in the first column
for h in range(length_col1):
    if col1[h] % 2 == 0 and col1[h] != 0:
        col1[h] = 0
        col2[h] = 0
    else:
        continue
#Sum the second column
answer = sum(col2)
#Output the final answer
print("The product of", ui_1, "and", ui_2, "is:", answer)
'''If I enter a enter a decimal my program is set up to convert it to an integer
right away because you wouldnt be able to carry out the steps(Halving until one)
with a flaot'''