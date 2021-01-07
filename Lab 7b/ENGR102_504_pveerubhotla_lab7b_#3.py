# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 7b-3
# Date:         12 OCTOBER 2019
#
'''This program returns a list containing all possible permutations of a string'''
#Take the user's input for the original String
ui = input("Please enter the string which the list of permutations will use:")
ui_copy = ui
final_list = []

#Using the String inputted by the user, construct a list containing the perms
def genPerms(ui):
   #If the length of the string is 1, return a list containing the String
   if len(ui) == 1:
       return [ui]
   #Create a list of permutations using charecters 2, 3...n
   perms = genPerms(ui[1::])
   #Seperate out the first charecter of the String
   first_char = ui[0]
   #Create a list to store the permutations
   perms_list = []
   #Iterate through the partial permutations
   for i in perms:
       #For each of the partial permutations, insert the first charecter at every index
       for j in range(len(perms) + 1):
           perms_list.append(i[:j] + first_char + i[j:])
   return perms_list

#Remove any possible duplicates from the output
permutations = genPerms(ui)
for k in permutations:
    if k not in final_list:
        final_list.append(k)

#Output the list of permutations for the user-entered String
print(final_list)