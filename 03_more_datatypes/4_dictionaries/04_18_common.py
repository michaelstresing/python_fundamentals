'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

""" I can't see why the following doesn't work... 

for k in dict_2:
    if k in dict_1:
        dict_1[k] = dict_1[k] + dict_2[k]

dict_3 = {**dict_1, **dict_2}

print(dict_3)
"""

from collections import Counter

result = Counter(dict_1) + Counter(dict_2)

print(result)