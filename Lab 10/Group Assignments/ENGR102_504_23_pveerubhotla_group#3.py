# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   Group Assignments #3
# Date:         27 OCTOBER 2019
#
'''This program counts the number of times a user input strings occurs in the file
'un.txt'.'''
#Take the user input for the String
ui = input("Please enter the string for which the text file will be searched for:")

#Open the text file, un.txt, for reading
un = open('un.txt', 'r')

data = un.readlines()
count = 0
for line in data:
    line2 = line.replace(',', '')
    line3 = line2.strip('.')
    line_split = line3.split(' ')
    for j in line_split: 
        j = j.lower()
        if ui == j:
            count += 1
    
print(count)