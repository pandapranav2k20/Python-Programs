# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-2e
# Date:         6 NOVEMBER 2019
#
'''This program shows the three ways of loading files.'''
import csv
import numpy as np
'''The directions were not very specific so I chose to simply load in the data.'''
#First way
def load1(file):
    data = open(file, 'r')
    lines = data.readlines()

#Second way
def load2(file):
    data = open(file, 'r')
    lines = csv.reader(data)

#Third way
def load3(file):
    data = np.genfromtxt(file, delimeter = '')