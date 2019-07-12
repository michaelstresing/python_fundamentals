'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

userput = input("Please enter some words: ")

inputtup = tuple(userput)

result_dict = {}

for i in inputtup:
    result_dict.update({i: inputtup.count(i)})

print(result_dict)