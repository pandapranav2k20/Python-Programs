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
# Converting meters per second to miles per hour

# user input of meters per second speed
speed_meps = float(input('Input meters per second speed: '))

# meter to miles
speed_mps = speed_meps * 0.0006214

# seconds to hours
speed_mph = speed_mps * 60 * 60

# conversion results
print(speed_meps,'meters per sencond equal\n' ,speed_mph,'miles per hour')


