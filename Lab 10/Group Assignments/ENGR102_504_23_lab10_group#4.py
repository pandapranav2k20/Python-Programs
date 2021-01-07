# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   Group Assignments #3
# Date:         27 OCTOBER 2019
#
'''This program writes all umique shared words between un.txt and doi.txt to 
matched.txt'''
#Open the 2 files for reading and the one file for writing
un = open('un.txt', 'r')
doi = open('doi.txt', 'r')
matched = open('matched.txt', 'w')

data1 = un.readlines()
data2 = doi.readlines()
new_list_1 = []
def removeChars(string):
    string = string.replace('.', '').replace('', '').replace('\n', '').replace(':', '')
    
un_lines = [i.strip().split(' ') for i in data1]
doi_lines = [j.strip().split(' ') for j in data2] 
intersection = []
for h in un_lines:
    if h in doi_lines:
        intersection += [h]