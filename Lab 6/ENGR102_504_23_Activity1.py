# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Damon Tran
#               Benson Nguyen
#               Matt Knauth
#               Pranav Veerubhotla
# Section:      504
# Assignment:   lab 6-1
# Date:         30 Sept 2019
''''This program uses the logic of Sheldon cooper to play a game of rock, paper,
scissors, lizard, spock'''
import random
#Create the list to store the game options
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
#Create an empty list to store the random selections for the player to use
choices = []
#Take the user input for number of players
ui = int(input("Please enter the number of players:"))

#Create a for loop to determine the choices for the players
for i in range(ui):
    j = i + 1
    x = random.choice(options)
    choices.append(x)
    print("Player", j, "chooses", x)
    
'''#Create a second loop to determine the winners
for h in choices:
    for k in choices:
        if h == "Rock":
            if k == "Rock":
                print("tie")
            if k == "Paper":
                print("Player", k, "covers", "player", h)
            if k == "Scissors":
                print("Player", h, "crushes", "player", k)
            if k == "Lizard":
                print("Player", )
            if k == "Spock":
                
        elif h == "Paper":
            if k == "Rock":
            if k =="Paper":
                print("tie")
            if k == "Scissors":
            if k == "Lizard":
            if k == "Spock":
            
        elif h == "Scissors":
            if k == "Rock":
            if k == "Paper":
            if k == "Scissors":
                print("tie")
            if k == "Lizard":
            if k == "Spock":
            
        elif h == "Lizard":
            if k == "Rock":
            if k == "Paper":
            if k == "Scissors":
            if k == "Lizard":
                print("tie")
            if k == "Spock":
            
        elif h == "Spock":
            if k == "Rock":
            if k == "Paper":
            if k == "Scissors":
            if k == "Lizard":
            if k == "Spock":
                print("tie")'''