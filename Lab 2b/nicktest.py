from math import *
#this program does 3D Linear Interpolation
#point 1, assume all distances in meters and all times in seconds
x1 = 1
y1 = 3
z1 = 7
time1 = 13
#point 2
x2 = 23
y2 = -5
z2 = 10
time2 = 84
#time we want to find the 3rd point at
targetTime = 50

def interpolate(finalTime, initialTime, finalDistance, initialDistance, evalTime):
    slope = (finalDistance - initialDistance)/(finalTime - initialTime)
    constant = (finalDistance) - slope * finalTime
    # y = m * x + b
    return slope * evalTime + constant

x3 = interpolate(time2, time1, x2, x1, targetTime)
y3 = interpolate(time2, time1, y2, y1, targetTime)
z3 = interpolate(time2, time1, z2, z1, targetTime)
print(x3)
print(y3)
print(z3)
