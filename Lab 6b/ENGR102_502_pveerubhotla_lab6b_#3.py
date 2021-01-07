# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-3
# Date:         30 SEPTEMBER 2019
#
'''This program finds the intersection between two lists, and saves it to a new 
list without using any list methods'''
import random
num_list1 = random.sample(range(1, 100), 30)
num_list2 = random.sample(range(1, 100), 30)
#Create a blank list to store the intersections between the two lists
intersection = []
#Calculate the intersection between the two lists
for i in num_list1:
    if i in num_list2:
        intersection += [i]
#If there is no intersection, output no intersection. Otherwise output the intersection
if len(intersection) == 0:
    print("There is no intersection between the lists")
else:
    print("The intersection between the two lists is:", intersection)