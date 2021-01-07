# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
#               DAMON TRAN
#               MATT KNAUTH
#               BENSON NGUYEN
# Section:      504
# Assignment:   lab 9-1
# Date:         21 OCTOBER 2019
#
'''Write a program that reads 'doi.txt' and writes all lines starting with 'he'
to 'he.txt', and all lines starting with 'for' to 'for.txt'''

doi = 'doi.txt'
he_start = 'he.txt'
for_start = 'for.txt'

orig_doc = open(doi, 'r')
he_doc = open(he_start, 'w')
for_doc = open(for_start, 'w')

data1 = orig_doc.readlines()


for i in data1:
    first_word = i.split(' ')[0] 
    i.join(" ")
    if first_word == 'He':
        he_doc.write(i)
    elif first_word == 'For':
        for_doc.write(i)