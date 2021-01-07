# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 10b-3
# Date:         27 OCTOBER 2019
#
import matplotlib.pyplot as plt
import pveerubhotla_504_VC as VC
#Store the vars we have so far, make news lists to store data
length_0 = 10
width_0 = 13
height_0 = 8
volumes = []
diameters = []
mass_remain = []
mass_removed = []

#Call the function the appropriate number of times and save the data
for dia in range(14):
    diameters.append(dia)
    volumes.append(VC.vol_calc_widget(length_0, width_0, height_0, dia/2))
    mass_remain.append((VC.vol_calc_widget(length_0, width_0, height_0, dia/2))*2.7)
    mass_removed.append(1040 * 2.7 - (VC.vol_calc_widget(length_0, width_0, height_0, dia/2))*2.7)

#Plot the data
fig1, ax1 = plt.subplots()
ax1.plot(diameters, volumes, label = 'Remaining Volume', color = 'green')
ax1.set_xlabel('Hole diameter (cm)')
ax1.set_ylabel('Volume (cm^3)')
ax1.legend(loc = 'upper right', frameon = True)
ax1.grid(linestyle = '-', linewidth = '0.5', color = 'black')

ax2 = ax1.twinx()
ax2.plot(diameters, mass_remain, label = 'Mass remaining', color = 'blue')
ax2.plot(diameters, mass_removed, label = 'Mass removed', color = 'orange')
ax2.set_ylabel('Mass (g)')
ax2.legend(loc = 'lower right', frameon = True)

plt.title('Hole diameter (cm) vs. Remaining volume (cm^3) and Mass (g)')
plt.show()

