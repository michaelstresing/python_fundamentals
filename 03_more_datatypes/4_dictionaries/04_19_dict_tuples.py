'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}

resulta = input_dict.items()
print(resulta)

resultb = []

for item in resulta:
    resultb.append(item)

print(resultb)

#Surely there's a more sophisticated solution to this....