# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Damon Tran
#               Benson Nguyen
#               Matt Knauth
#               Pranav Veerubhotla
# Section:      504
# Assignment:   lab 4-1
# Date:         16 Sept 2019
'''This program will create 5 instances of roundoff errors'''
import math
#Test the first segment of code provided to us
'''a = 1/7
print(a)
b = a * 7
print(b)'''

#Test the second segment of code provided to us
'''a = 1/7
print(a)
b = 7 * a
print(b)
c = 2 * a
d = 5 * a
e = c + d
print(e)'''

#Test the third segment of code provided to us
'''x = math.sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)'''

#Part 1: create the five roundoff errors
#roundoff error 1
error1 = math.sin(math.pi/4)
print("Is sin(pi/4) the same as math.sqrt(2)/2?", 1==2)

#roundoff error 2
error2 = math.tan(math.pi/4)
print("Is tan(pi/4) the same as 1?", 1==2)

#roundoff error 3
error3 = math.cos(math.pi/2)
print("Is cos(pi/2) the same as 0?", 1==2)

#roundoff error 4
error4 = 0.1 + 0.2
print("Is 0.1 + 0.2 the same as 0.3?", 1==2)

#roundoff error 5
error5 = math.cos((-1 * math.pi)/2)
print("Is cos(-pi/2) the same as 0?", 1==2)

#Farthest away from actual number
#print(error2**2137134182319283129389102381083012)

#Part 2: Tolerances for comparisons
tolerance = 10**-9
#tolerance check 1
a = math.sin(math.pi/4)
b = math.sqrt(2)/2
if abs(a-b) <= tolerance:
    result  = True
else:
    result = False
print("Is spin(pi/4) within tolerance of math.sqrt(2)/2", result)

#tolerance check 2
a = math.tan(math.pi/4)
b = 1
if abs(a-b) <= tolerance:
    result  = True
else:
    result = False
print("Is tan(pi/4) within tolerance of 1", result)

#tolerance check 3
a = math.cos(math.pi/2)
b = 0
if abs(a-b) <= tolerance:
    result  = True
else:
    result = False
print("Is cos(pi/2) within tolerance of 0", result)

#tolerance check 4
a = 0.1 + 0.2
b = 0.3
if abs(a-b) <= tolerance:
    result  = True
else:
    result = False
print("Is 0.1 + 0.2 within tolerance of 0.3", result)

#tolerance check 5
a = math.cos((-1 * math.pi)/2)
b = 0
if abs(a-b) <= tolerance:
    result  = True
else:
    result = False
print("Is cos(-pi/2) within tolerance of 0", result)

#Part 3: Tolerances for sizes
#print a line to seperate output from the rest of the code
print("-----------------------------------------")
tolerance = 10**-16
print("The tolerance is equal to:", tolerance)
a = math.sin(math.pi/4)
print("A is equal to:", a)
b = math.sqrt(2)/2
print("B is equal to:", b)
x = 1/123456789999999999999
print("X is equal to:", x)
y = 1/123456789999999999998
print("Y is equal to:", y)
if abs(a-b) <= tolerance:
    result_ab = True
    print("A and B are within the tolerance.", result_ab)
else:
    result_ab = False
    print("A and B are not within the tolerance.", result_ab)
if abs(x-y) <= tolerance:
    result_xy = True
    print("X and Y are within the tolerance.", result_xy)
else: 
    result_xy = False
    print("X and Y are not within the tolerance.", result_xy)