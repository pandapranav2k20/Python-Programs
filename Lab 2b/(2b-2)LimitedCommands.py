# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB2b-3
# Date: 7 September 2019
'''x = 1
y = 10
z = 0
x = y
x += 1
y += x
y *= x
z += x
z += y
print(z)'''
#my code begins below
#z must equal 1
x = 1
z = 0
z += x
#print the value of z
print(z)

#z must equal 3
z += x
z += x
#print the value of z
print(z)

#z must equal 11
y = 10
z = 0
z += x
z += y
#print the value of z
print(z)

#z must equal 28
x += 1
x += 1
x += 1
y += x
x = 1
x += 1
y *= x
z = 0
z += y
#print the value of z
print(z)

#z must equal 123
#get to 100 first
y = 10
x = y
y *= x
z = 0
z += y
#get to 23
x = 1
x += 1
y =10
y *= x
x += 1
y += x
z += y
#print the value of z
print(z)

#z must equal 10^32
y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z = 0
z += y
#print the value of z
print(z)

#z must equal 4321
#get to 4000 first
y = 10
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
y *= x
z = 0
z += y
#get to 4300
y = 10
x = y
y *= x
x = 1
x += 1
x += 1
y *= x
z += y
#get to 21
y = 10
x = 1
x += 1
y *= 2
x = 1
y += x
z += y
#print the value of z
print(z)
