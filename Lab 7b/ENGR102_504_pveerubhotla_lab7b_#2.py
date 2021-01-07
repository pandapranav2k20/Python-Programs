# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 7b-2
# Date:         12 OCTOBER 2019
#
'''This program does various calculations for two user entered vectors, A and B'''
import math
#Take the user input for the appropriate number of dimensions
num_dims = int(input("Please enter the number of dimensions for the vectors"))
#Initialize the vvars/lists we will store values in later
vec_A = []
vec_B = []
mag_A = 0
mag_B = 0
vec_AplusB = []
vec_AminusB = []
dot_prod = 0
#Promt the user to enter the component for vectors A and B based upon num_dims
for i in range(0, num_dims):
    str_a = "Please enter component " + str(i + 1) + " of Vector A: " 
    str_b = "Please enter component " + str(i + 1) + " of Vector B: " 
    current_element_a = float(input(str_a))
    current_element_b = float(input(str_b))
    vec_A.append(current_element_a)
    vec_B.append(current_element_b)

#Find the magnitude of A and B    
for h in range(0, num_dims):
    mag_A += vec_A[h]**2 
    mag_B += vec_B[h]**2 
#Take the square root of the previous calculation to find the magnitude
mag_A = math.sqrt(mag_A)
mag_B = math.sqrt(mag_B)

#Find the sum of the vectors
for j in range(0, num_dims):
    sum_component = vec_A[j] + vec_B[j]
    vec_AplusB.append(sum_component)
    
#Find the diffirence of the vectos
for k in range(0, num_dims):
    diff_component = vec_A[k] - vec_B[k]
    vec_AminusB.append(diff_component)
    
#Calculate the dot product between the two vectors
for l in range(0, num_dims):
    dot_prod += vec_A[l] * vec_B[l]
#Finally divide the previous calculation by the product of the magnitudes
dot_prod = dot_prod / (mag_A * mag_B)

#Output all the desired calculations
print("The magnitude of vector A is:", mag_A)
print("The magnitude of vector B is:", mag_B)
print("A + B =",vec_AplusB)
print("A - B =", vec_AminusB)
print("The dot product of A*B =", dot_prod)
