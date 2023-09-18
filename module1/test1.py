'''
Lists
--Examples
'''

if True:
    print('Its True')

# doesn't print? The statement in the if is converted to a bool
if False:
    print('Its True!')


# flat is better than nested
p = 17
if p > 20:
    print('Greater than 20')
elif p < 10:
    print('Less than 10')
else:
    print('In the middle')


#while loops
V = 1
while V < 5:
    print(V)
    V += 1
    

# exist loop when V is 3    
V = 1
while V < 5:
    print(V)
    if V == 3:
        break
    V += 1   



    
