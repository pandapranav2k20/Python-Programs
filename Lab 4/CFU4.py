# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   CFU 4
# Date:         18 SEPTEMBER 2019
#
#This program calculates an outputs students final grades given their HW score, Exam score, and participation in an ec project
#Take the user input
hw_score = float(input("Please enter your Homework score:"))
exam_score = float(input("Please enter your Exam score:"))
#Store whether they completed the project as a boolean
project = bool(int(input("Please enter a zero if you have not completed the project and a 1 if you have:")))

#Calculate the students grade
grade = 40 * hw_score + 60 * exam_score
#Add the extra credit to their grade if applicable
if project:
    grade += 5
#Output their grade
if grade >= 90:
    if project:
        print("You have an A in the class")
    else:
        print("You have a B in the class")
if 80 <=grade<= 90:
    print("You have a B in the class")
if 70 <=grade<= 80:
    print("You have a C in the class")
if 60 <=grade<= 70:
    print("You have a D in the class")
if 60 > grade:
    print("You have an F in the class")