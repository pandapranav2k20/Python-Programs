# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-1
# Date:         30 SEPTEMBER 2019
#
'''This program that removes duplicates from a user inputted list, the program will then return 
the original list, the list of duplicates, and the list of unique numbers'''
#Take user input for the list
ui = input("Please enter the first value of the list:")
print("Hit enter when you have finished entering values")
orig_list = []
#Continue asking the user to input the next value until the user enters ''
while ui != '':
    orig_list.append(ui)
    ui = input("Please enter the next value of the list:")

#Make and store a copy of the original list
copy_orig = []
copy_orig += orig_list

#Remove the duplicates from the original list and add then to the list no_dupes
def remove_dupes(copy_orig):
    no_dupes =[]
    for num in copy_orig:
        if num not in no_dupes:
            no_dupes.append(num)
    return no_dupes

#Create a blank list to find the duplicate values
dupes =[]
#Use a for loop to locate the values that occur more than once and add them to the list dupes
for i in copy_orig:
    if copy_orig.count(i) > 1:
        copy_orig.remove(i)
        dupes.append(i)

#Output the lists of: original values, duplicate values, and unique values
print("The list of unique values is:", remove_dupes(copy_orig))
print("The list of duplicate values is:",dupes)
print("The original list is:", orig_list)