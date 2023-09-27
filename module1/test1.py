# Argument Passing

m = [2,3,45,17,89]
def modify(k): 
    k.append(77)
    print('K =', k)

modify(m)    

print(m) #77 is appended to the list



V = [4,6,7]
def replace(l):
    l = [5,7,88] #completely new list
    print('L is', l)

replace(V)
print(V) 

#default augument values
def banner(message, border='-'): #callers of the function decide whether to use the default
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('Germany')   

banner('Germany, Austria', '*')

banner('South, North, East', border = '*') #position argument and keyword argument respectively

banner(border = '!', message = 'True') #both keyword arguments

# rebinding global names
count = 0 # module scope
def show_count():
    print(count)

def set_count(a):
    global count
    count = a
    print(count)

show_count()
set_count(7)
show_count() #prints out 7 since count is globally scoped


#built-in collections
#tuples -immutable sequences of arbitrary objects

t = ('')
