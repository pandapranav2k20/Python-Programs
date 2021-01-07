# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   lab 7-1
# Date:         4 OCTOBER 2019
#
'''Write a program that counts the number of vowles in a user inputted string'''
#Take the user input for the string
ui_string = input("Please enter the string:")
ui_string_copy = ""
ui_string_copy += ui_string
uppercase = ""
vowels = ["a","e","i","o","u","A","E","I","O","U"]
num_vowels = 0
for i in ui_string:
    if i in vowels:
        num_vowels += 1
        if i == "a":
            uppercase = ui_string_copy.replace("a", "A")
        elif i == "e":
            uppercase = ui_string_copy.replace("e", "E")
        elif i == "i":
            ui_string_copy.replace("i", "I")
        elif i == "o":
            uppercase = ui_string_copy.replace("o", "O")
        elif i == "u":
            ui_string_copy.replace("u", "U")

#Output the number of vowels in the string and the string with the vowels uppercase
print("There are", num_vowels, "vowels in the string", ui_string)
print("The string with uppercase vowels is:", uppercase)

        