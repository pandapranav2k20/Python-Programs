# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   Lab 4b-3
# Date:         18 SEPTEMBER 2019
#
#This porgram reads in data and computes the reynolds number
#Take in user input for al the required data
fliud_velocity = int(input("Please enter the value for fluid velocity:"))
kinematic_viscosity = int(input("Please enter the value for kinematic viscosity"))
char_lin_dimension = int(input("Please enter the charecteristic linear dimension:"))
#Calculate the reynolds number 
def calcReNum(fliud_velocity, kinematic_viscosity, char_lin_dimension):
    reNum = 7745.8 * fliud_velocity * (char_lin_dimension / kinematic_viscosity)
    return reNum
#Determine whether flow is laminar,transition, or turbulent
if calcReNum(fliud_velocity, kinematic_viscosity, char_lin_dimension) < 2300:
    flow = 'laminar'
elif calcReNum(fliud_velocity, kinematic_viscosity, char_lin_dimension) <= 4000:
    flow = 'transistent'
elif calcReNum(fliud_velocity, kinematic_viscosity, char_lin_dimension) >4000:
    flow = 'turbulent'
#Output the flow and the source for the break points
print("The flow is", flow, "https://www.engineeringtoolbox.com/laminar-transitional-turbulent-flow-d_577.html")