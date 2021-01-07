fname = 'cable.txt'


'''for i in range(5):
    xtra = 'We are the Knights of Nee\n'
    fh.write(xtra)
fh.close()'''

with open(fname, 'r') as fh:
    all_stuff = fh.read()
    
print(all_stuff)
