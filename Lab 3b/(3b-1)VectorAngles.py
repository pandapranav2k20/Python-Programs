# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3b-1
# Date: 12 September 2019
'''This program will take user input for 3 3D points and calculate the angle 
between the points from an accurate perspective, output in degrees'''
import math
#take the input from the user
observer_pos = list(input("Please enter the position of the observer in (x, y, z)."))
first_point = list(input("Please enter the position of the first point (x, y, z)."))
sec_point = list(input("Please enter the position of the second point (x, y, z)."))
#calculate the two vectors
#calculate all the components for vector one
x1 = int(first_point[1]) - int(observer_pos[1])
y1 = int(first_point[4]) - int(observer_pos[4])
z1 = int(first_point[7]) - int(observer_pos[7])
#calculate all the components for vector two
x2 = int(sec_point[1]) - int(observer_pos[1])
y2 = int(sec_point[4]) - int(observer_pos[4])
z2 = int(sec_point[7]) - int(observer_pos[7])
#Normalize the vectors
#Calculate the magnitudes of the two vectors first
Magnitude_1 = math.sqrt(x1**2 + y1**2 + z1**2)
Magnitude_2 =math.sqrt(x2**2 + y2**2 + z2**2)
#Normalize each component of each vector
x1_norm = x1 / Magnitude_1
y1_norm = y1 / Magnitude_1
z1_norm = z1 / Magnitude_1
x2_norm = x2 / Magnitude_2
y2_norm = y2 / Magnitude_2
z2_norm = z2 / Magnitude_2
#Calculate the dot product between the vectors
#a*b = a1b1 + a2b2 + a3b3
Dot_prod_v1v2 = x1_norm * x2_norm + y1_norm * y2_norm + z1_norm * z2_norm
#Calculate the angle between the two vectos using the dot product
ang_v1v2 = math.acos(Dot_prod_v1v2/(Magnitude_1 * Magnitude_2))
#Output the angle in degrees
ang_v1v2_deg = ang_v1v2 * (180/math.pi)
print("The angle between the two vectors is: ", ang_v1v2_deg, "degrees.")