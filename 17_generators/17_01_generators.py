'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen = (x for x in range(100))

print(gen)

for x in gen:
    print(x)