'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

#reference: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []

for list in starting_list:
    for item in list:
        flattened_list.append(item)

print(flattened_list)
