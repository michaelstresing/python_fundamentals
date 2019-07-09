'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string_ = input("Please enter a bunch of words: ")
slist = string_.split()
print(slist)

#referenced https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item

from collections import Counter
counts = Counter(slist)
popular = counts.most_common(1)
print("counter most popular", popular)

''' Trying to setup where we create a tally sorted by most popular, then print the first item in the tally -> Stuck
def takeSecond(elem):
    return elem[1]

tally = [[x,slist.count(x)] for x in set(slist)]
tally.sort(key = takeSecond)

print("tally most popular", tally[0])
'''