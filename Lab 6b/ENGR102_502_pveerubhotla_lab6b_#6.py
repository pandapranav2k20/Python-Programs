# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   lab 6b-6
# Date:         30 SEPTEMBER 2019
#
'''This program uses dictionaries to store sets of usernames and passwords(amount
is specified by the user), then allow the user to type a username and password,
if they have the correct combination, allow them to enter the system'''
#Request the user on how many sets of user/pass they would like to enter
num_sets = int(input("Please enter the number of usernames/passwords to enter:"))

#Create blank lists to store the usernames and passwords
usernames = []
passwords = []

#Request the user to enter the appropriate number of usernames
for i in range(num_sets):
    u_prompt_str = "Please enter username " + str(i+1) + ":"
    ui_user = input(u_prompt_str)
    usernames.append(ui_user)

#REquest the user to type the appropriate number of passwords
for j in range(num_sets):
    p_prompt_str = "Please enter password " + str(j+1) + ":"
    ui_pass = input(p_prompt_str)
    passwords.append(ui_pass)
    
#Converts the two lists(users/pass) to a single dictionary called sets
def convert(usernames, passwords):
    sets = dict(zip(usernames, passwords))
    return sets

#Save the sets in user_pass_vault
user_pass_vault = convert(usernames, passwords)

#Request the user to enter a username
ui_attempt_user = input("Please enter a username:")
#If the username is not in the dictionary, ask them to enter a valid username
while(ui_attempt_user not in user_pass_vault):
    ui_attempt_user = input("Please enter a valid username:")

'''Determine if the user can enter the system'''
#If they enter a valid username, ask them to enter a password
if ui_attempt_user in user_pass_vault:
    ui_attempt_pass = input("Please enter the password:")
    #If the password is incorrect, promt the user to continue entering passwords
    while(ui_attempt_pass != user_pass_vault.get(ui_attempt_user)):
        print("That password is incorrect")
        ui_attempt_pass = input("Please enter the correct password:")
    #If the user/pass match up with a key and value in the dict, allow the user to enter
    if ui_attempt_pass == user_pass_vault.get(ui_attempt_user):
        print("You have been allowed into the system!")