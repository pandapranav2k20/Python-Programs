# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 11b-3
# Date:         6 NOVEMBER 2019
#
'''This function takes in a coefficient matrix and a solution vector and solves
the system of equations using linear algebra.'''
import numpy as np

def linAlg(coefficients, solutions):
    sol = np.linalg.solve(coefficients, solutions)
    if len(sol) > 0:
        return sol
    else:
        print('No solution exists')
    
a =  np.array([[1,1],[1,-1]])
b = np.array([[4],[2]])

print(linAlg(a, b))