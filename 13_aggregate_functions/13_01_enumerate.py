'''
Demonstrate the use of the .enumerate() function.
'''

#from the python docs on how it functions:

def enum_function(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

#demonstration

mydinner = ['Peas', 'Potatoes', 'Carrots', 'Steak']

iate1 = enumerate(mydinner, start=1)

iate2 = enum_function(mydinner, start=1)

print(list((iate1)), list(iate2))