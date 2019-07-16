'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
#this one wasn't fair...
import operator
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

unsorted_list.sort(key= operator.itemgetter(1))

print(unsorted_list)


#almost all solutions I could find involved itemgetter/lambdas
#this was the best bet:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

def key(item):
    return item[1]

sorted_list = sorted(unsorted_list, key= key)

print(sorted_list)

#tried the following variations, all of them didn't work...

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sortedlist = []

for tuple in unsorted_list:
    list1 = [tuple]

for list1 in unsorted_list:
    sortedlist.sort(unsorted_list, key= list1[1])

print(sortedlist)

#or...(I figured this'd work)

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sortedlist = []

for tuple in unsorted_list:
    key = tuple[1]

for list1 in unsorted_list:
    sortedlist.sort(unsorted_list, key= key)

print(sortedlist

