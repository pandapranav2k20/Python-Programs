# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Benson Nguyen
#               Pranav Veerubhotla
#               Jolie Hand
#               Emily Hotz
# Section:      504
# Assignment:  Lab3
# Date:         11 Sep 2019
# Converting Miles per Hour to Meters per Second

# user input of miles per hour speed
speed_mph = float(input('Input miles per hour speed: '))

# miles to meters
speed_meph = speed_mph * 1609.34

# hours to seconds
speed_meps = speed_meph / 60 / 60

# conversion results
print (speed_mph, 'miles per hour equals\n',speed_meps,'meters per second')

