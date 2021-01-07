# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB2-1
# Date: 7 September 2019
from math import *
#program does same things as EngineeringEquations.py but utilizes pythons ability to print vars instead
print('no answer')#prints 'no answer'
print('Pranav Veerubhotla', '128007104', '504')#prints name, UIN, section number
print('I love working on cars and I drive a 2001 Mazda Miata named Katie.')#prints an interesting fact about myself

#ohms law: V=IR
#declare the vars needed for the calculation
resistance = 20
current = 5
#calculate the volatage and store in var volts
volts = 5 * 20
#add units to the voltage calculated above
volts_units = str(volts) + " volts"
#print the final volatage calculated along with units as a string
print(volts_units)

#kinetic energy = (1/2)mv**2
#declare the vars needed for the calculation
mass_kg = 100
velocity_mps = 21
#calculate the kinetic enercy and store in var kinetic_energy
kinetic_energy = (1/2)*(mass_kg)*(velocity_mps**2)
#add units to the Kinetic energy calculated above
kinetic_energy_units = str(kinetic_energy) + " joules"
#print the final kinetic energy calculated along with units as a string
print(kinetic_energy_units)

#Re = 7745.8*u*(dh/v)
#declare the vars needed for the calculation
velocity_mps = 100
kinematic_viscosity_m2 = 1.2
charercteristic_linear_dimension_m = 2.5
#convert the vars to correct units for fomula
velocity_fps = velocity_mps * 3.28084
kinematic_viscosity_cst = kinematic_viscosity_m2/(10**-6)
charercteristic_linear_dimension_in = charercteristic_linear_dimension_m * 3.28084 *12
#calculate the Reynolds Number from the variables above and stores in var reynolds_num
reynolds_num = 7745.8 * velocity_fps * (charercteristic_linear_dimension_in / kinematic_viscosity_cst)
#adds units to the reynolds number calculated above
reynolds_num_fin = "Reynolds Number: "+ str(reynolds_num)
#print the final Reynolds number along with units as a string
print(reynolds_num_fin)

#q(t)=(qi)/((1+bDit)**(1/b))
#declare the variables needed for this calculation
qi_bpd = 100
b = 0.8
di_bpd = 2
t_day = 20
#calculate the rate of production of barrels after 20 days
qt = qi_bpd/((1 + b * di_bpd * t_day)**(1/b))
#add units to the above calculation
qt_bpd = str(qt) + " barrels per day"
#print the final production of barrels after 20 days with units as a string
print(qt_bpd)

print('no answer')#prints 'no answer'

#t=sigma*tan(theta)+c
#declare the var needed for the calculation
sigma_lbfpin2 = 20
theta_rads = 35
c_lbfpin2 = 2
# calculate the sheer stress and store in the var sheer_stress
sheer_stress = sigma_lbfpin2 * tan(theta_rads) + c_lbfpin2
#add units to the sheer stress calculation above
sheer_stress_lbfpin2 = str(sheer_stress) + " lbf/in^2"
#print the sheer stress witht the units attatched as a string
print(sheer_stress_lbfpin2)