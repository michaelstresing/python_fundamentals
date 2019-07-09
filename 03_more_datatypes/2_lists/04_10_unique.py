'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
uniquelist = list(set(list_))

print(uniquelist)

#alternative possibility?

uniquelist2 = []

for item in list_:
    if item not in uniquelist2:
        uniquelist2.append(item)

print(uniquelist2)

#it looks like the first option will sort, whilst the second keeps the order of the original list