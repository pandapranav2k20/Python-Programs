# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 7b-1
# Date:         11 OCTOBER 2019
#
'''This program converts user enetered strings into Pig Latin'''
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
punctuation = ["!","?",".",",",":",";"]
pig_latin = []
cons_index = 0
#Take user input for the Strings to be converted
ui_strings = []
ui = input("Please enter a String to be converted:")
while(ui != "stop"):
    #If the user enters a sentence, split it into words
    ui_split = ui.split(" ")
    #Remove any possible punctuation from the new list contaning split words
    for i in ui_split:
        for j in i:
            if j in punctuation:
                new_i = i.replace(j, '')
                index = ui_split.index(i)
                ui_split[index] = new_i
    #Add the new de-punctuated, split elements from the sentence to ui_strings
    ui_strings += ui_split
    ui = input("Please enter the next string, type 'stop' to exit:")

#Convert the user entered strings into Pig Latin
for i in ui_strings:
    first_letter = i[0]
    second_letter = i[1]
    #If the given string in ui_strings starts with 2 consonants
    if first_letter not in vowels and second_letter not in vowels:
        i = i[2:len(i)] + i[0] + i[1]
        ending = "ay"
        pig_latin.append(i + ending)
    #If the given string in ui_strings starts with 1 consonant
    elif first_letter not in vowels:
        i = i[1:len(i)] + i[0]
        ending = "ay"
        pig_latin.append(i + ending)
    #If the given string in ui_strings begins with a vowel
    elif first_letter in vowels:
        ending = "yay"
        pig_latin.append(i + ending)

#Output the list of words converted into Pig Latin
print("The list of Pig Latin words is:", pig_latin)