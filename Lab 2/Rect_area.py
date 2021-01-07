# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: PRANAV VEERUBHOTLA
# Section: 504
# Assignment: LAB1B-2
# Date: 2 September 2019

#Program to calculate cross section of pin

#Break pin into two rectangles(Pca_rect1 and Pca_rect2)
#Break is to the right of the 6cm section
#Define length and Width

#Variables for Pca_rect1
PcaLength_rect1 = 12 #cm
PcaWidth_rect1 = 6 #cm

#Variables for Pca_rect2
PcaLength_rect2 = 5 #cm
PcaWidth_rect2 = 10 #cm

#Caclulates the area of Rectangles
#Area = legth * width
#Calculate the area of Pca_rect1
Pca_rect1_Area = PcaLength_rect1 * PcaWidth_rect1 #cm**2

#Calculate the area of Pca_rect2
Pca_rect2_Area = PcaLength_rect2 * PcaWidth_rect2 #cm**2

#Sum the areas of the rectangles
Pca_sum_Area = Pca_rect1_Area + Pca_rect2_Area #cm**2

#Display the results
print('The cross sectional area of the pen is:', Pca_sum_Area, 'cm**2')