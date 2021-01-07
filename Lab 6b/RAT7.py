# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      540
# Assignment:   RAT 7
# Date:          7 Oct 2019
#
L2 = []
L1 = [5, 3.1415, "Go Dog Go", tuple((3,4, "cable"))]
L2 += L1
L2.append("What, a swallow carrying a coconut?")
L_prime = []
L_reverse =[]
for i in range(10, 31):
    if i%2 != 0 and i%3 != 0 and i%5 != 0:
        L_prime.append(i)
def convert(L_prime):
    T1 = tuple(L_prime)
    return T1

a = convert(L_prime)
print(a)
L3 = [L1[0], L1[1], L2[-1]]

for j in range(len(convert(L_prime))):
    if j %2 == 0:
        L_reverse.append(a[j])

T2 = convert(L_reverse).reverse()