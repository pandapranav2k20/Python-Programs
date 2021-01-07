# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         PRANAV VEERUBHOTLA
# Section:      504
# Assignment:   CFU 10
# Date:         30 OCTOBER 2019
#
un = open('un.txt', 'r')

data = un.readlines()
num_lines = 0
total_words = 0
unique_words = []
words_nums = []
num_times = 0
for i in data:
    num_lines += 1
    i = i.replace(',', '').replace('.', '').replace('\n', '').replace(':', '')
    i = i.split(' ')
    for word in i:
        total_words += 1
        if word not in unique_words:
            unique_words.append(word)

for j in data:
    j = j.replace(',', '').replace('.', '').replace('\n', '').replace(':', '')
    j = j.split(' ')
    for word2 in j:
        for h in unique_words:
            if h == word2:
                num_times += 1
        a = (h, num_times)
        words_nums.append(a)
            #words_nums.append(tuple(h, num_times))
            
      
print("The total number of lines is:", num_lines)
print("The total number of words is:", total_words)           
print(words_nums)

un.close()