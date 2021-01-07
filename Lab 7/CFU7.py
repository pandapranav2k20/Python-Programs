# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   CFU 6
# Date:         9 OCTOBER 2019
#
import random
num_list1 = random.sample(range(1, 100), 30)
num_list1.sort()

#Find the median of the list
#If the list has an even length
if len(num_list1) % 2 == 0:
    m1 = num_list1[int(len(num_list1)/2)]
    m2 = num_list1[int(len(num_list1)/2 - 1)]
    median = (m1 + m2)/2
#If the list has an odd length
else:
    median = num_list1[len(num_list1)//2]

#Find the largest even and odd number
larg_even = 0
larg_odd = 0
for i in num_list1:
    if i > larg_even and i%2 == 0:
        larg_even = i
    if i > larg_odd and i%2 != 0:
        larg_odd = i
        
#Output the data from the calculations
print("The Median is:", median)
print("The largest even number is:", larg_even)
print("The largest odd number is:", larg_odd)
print("The list sorted is:", num_list1)