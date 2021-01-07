# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB3-4
# Date: 11 September 2019
 
#Inputs taken in for the Mad-Lib
season = input("Please enter the season: ")
verb_ed = input("Please enter an verb ending in -ed: ")
food = input("Please enter a food: ")
shoe_size = float(input("Please enter a shoe size: "))
animal = input("Please enter an animal: ")

#create the sentences for the story
print("It was during a foggy", season, '''morning when Binglius realized it was his birthday. 
Caught by surprise, Binglius contemplated how to spend his day. The previous year, Binglius
was forced to attend a send off party. Binglius''', verb_ed, "and", verb_ed, '''for so long,
at the end of the day he could barely walk in a straight line \n 
Determined to make his birthday better than last year he headed to his computer in order to do some shopping. 
In his haste, Binglius spilled his''', food, '''all over his computer. After finally cleaning up his mess,
Binglius decided that he wanted to buy a new pair of shoes, Binglius headed to amazon and began searching. 
After hours of dedicated labor, he had finally picked out the pair, but first he needed to convert his shoe size.
After googling the conversion rate between Uk and US shoe sizes, Binglius was finally ready. He converted his size''',
shoe_size, "US shoe to a size", shoe_size - 0.5, '''Uk. He added the shoes to his wheelbarrow
and was getting ready for checkout. He had just one last obstacle in his path, the dreaded captcha!
The captcha's directions read 'please select all boxes with animals in them', as Binglius
stared at the screen he realized that one box had a''', animal, '''in it. After much consideration
he finally decided that''', animal, '''was indeed an animal. Two weeks later Binglius finally recieved his
birthday shoes in the mail''')