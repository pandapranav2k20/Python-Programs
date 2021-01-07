# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 7b-4
# Date:         12 OCTOBER 2019
#
'''This program seperates a paragraph of text into a list of unique words'''
punctuation = ["!","?",".",",",":",";"]
final_list = []
#Take the user input for the block of text to be seperateed
ui = input("Please enter the text to be seperated:")

#Split the paragraph into a list of words, seperating at spaces
words = ui.split(" ")

#Remove any punctuation from the elements of words, excluding apostrophes
for i in words:
    for j in i:
        if j in punctuation:
            new_i = i.replace(j, '')
            index = words.index(i)
            words[index] = new_i

#Create a list containing only the unique elements of words
for k in words:
    if k not in final_list:
        final_list.append(k)

#Output the final list
print(final_list)