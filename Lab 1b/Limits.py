# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB1B-2
# Date: 8 AUGUST 2019
from math import *
#function number one
print('This shows the evalutaion of f(x) = sin(x)/x) evaluated close to x=0.')#prints purpose of function
print('I think f(x) will approach 0.')#prints my guess
x = 1#sets the base value upon which the number sequence will be generated
print(sin(x)/x)#calculates f(1)
print(sin(x*10**-1)/(x*10**-1))#calculates f(1x10^-1)
print(sin(x*10**-2)/(x*10**-2))#calculates f(1x10^-2)
print(sin(x*10**-3)/(x*10**-3))#calculates f(1x10^-3)
print(sin(x*10**-4)/(x*10**-4))#calculates f(1x10^-4)
print(sin(x*10**-5)/(x*10**-5))#calculates f(1x10^-5)
print(sin(x*10**-6)/(x*10**-6))#calculates f(1x10^-6)
print(sin(x*10**-7)/(x*10**-7))#calculates f(1x10^-7)
print('')

#function number two
print('This shows the evaluation of g(x)=(1-cos(x))/(x**2) evaluated close to x=0.')#prints purpose of function
print('I think g(x) will approach 0.5.')#prints my guess
print((1-cos(x))/(x**2))#calculates g(1)
print ((1-cos(x*10**-1))/((x*10**-1)**2))#calculates g(1x10^-1)
print ((1-cos(x*10**-2))/((x*10**-2)**2))#calculates g(1x10^-2)
print ((1-cos(x*10**-3))/((x*10**-3)**2))#calculates g(1x10^-3)
print ((1-cos(x*10**-4))/((x*10**-4)**2))#calculates g(1x10^-4)
print ((1-cos(x*10**-5))/((x*10**-5)**2))#calculates g(1x10^-5)
print ((1-cos(x*10**-6))/((x*10**-6)**2))#calculates g(1x10^-6)
print ((1-cos(x*10**-7))/((x*10**-7)**2))#calculates g(1x10^-7)
print('')

#function number three
print('This shows the evaluation of h(x)=(1+(1/x))**x evaluated close to x = infinity.')#prints purpose of function
print('I think h(x) will approach infinity at x = infinity.')#prints my guess
print((1+(1/x))**x)#calculates h(1)
print((1+(1/(x*10**1)))**(x*10**1))#calculates h(1x10^1)
print((1+(1/(x*10**2)))**(x*10**2))#calculates h(1x10^2)
print((1+(1/(x*10**3)))**(x*10**3))#calculates h(1x10^3)
print((1+(1/(x*10**4)))**(x*10**4))#calculates h(1x10^4)
print((1+(1/(x*10**5)))**(x*10**5))#calculates h(1x10^5)
print((1+(1/(x*10**6)))**(x*10**6))#calculates h(1x10^6)
print((1+(1/(x*10**7)))**(x*10**7))#calculates h(1x10^7)
