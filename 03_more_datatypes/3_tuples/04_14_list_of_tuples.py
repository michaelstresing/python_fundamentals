'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

userput = input("Please input string: ")

slist = userput.split()

newlist = []

for i in slist:
    newlist.append(tuple(list(i)))

print(newlist)