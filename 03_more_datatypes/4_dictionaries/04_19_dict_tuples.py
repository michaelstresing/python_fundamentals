'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = []

for key, value in input_dict.items():
    result_list.append((key, value))


def sort(item):
    return (item[1])

list2 = sorted(result_list, key= sort)

print(list2)


#oddly... << list2 = result_list.sort(result_list, key= sort) >> didn't work. I was under the impression that sorted() and .sort were the same?