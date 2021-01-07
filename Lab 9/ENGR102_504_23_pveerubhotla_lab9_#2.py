# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
#               DAMON TRAN
#               MATT KNAUTH
#               BENSON NGUYEN
# Section:      504
# Assignment:   lab 9-1
# Date:         21 OCTOBER 2019
#
'''This program reads a temperature file and creates a number of lists. The first
list containts the cities, the second contains the units. The numeric data is in
columns corresponding to the cities, the data should be loaded to a list as well'''

temp = 'temp.csv'
list1, list2, list3 = [], [], []
orig_doc = open(temp, 'r')


cities = orig_doc.readline()
units = orig_doc.readline()

#Create list 1
cities_split = cities.split(',')
for i in cities_split:
    list1.append(i)

#Create list 2
units_split = units.split(',')
for j in units_split:
    list2.append(j)

day, c1, c2,c3, c4, c5, c6 = [], [], [], [], [], [], []
#Create list 2
for x in orig_doc:
    day.append(x.split(',')[0])
    c1.append(x.split(',')[1])
    c2.append(x.split(',')[2])
    c3.append(x.split(',')[3])
    c4.append(x.split(',')[4])
    c5.append(x.split(',')[5])
    c6.append(x.split(',')[6])
    
list3 += day, c1, c2, c3, c4, c5, c6
print(list1, '\n', list2, '\n', list3)