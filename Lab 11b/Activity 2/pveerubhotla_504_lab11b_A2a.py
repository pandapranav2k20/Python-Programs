# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-2
# Date:         6 NOVEMBER 2019
#
'''This program uses numpy arrays and methods to find the n largest values of 
an array.'''
import numpy as np

#ui = input('Please enter findNLargest followed by parameters in parentheses:')

def findNLargest(array, n):
    nLargest = []
    largest = -999
    while len(nLargest) <= n:
        for i in array:
            if i > largest:
                largest = i
                array.remove(i)
        nLargest.append(largest)
    print('The', n, 'largest numbers in the array were:', nLargest)

'''dispatcher = { 'findNlargest' : findNLargest}

def call_func(x, y, func):
    try:
        return dispatcher[func](x, y)
    except:
        return "Invalid function"

call_func(2, 3, 'f)'''