'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

text = input("Enter a sentence: ")
symbol = input("Please enter a symbol: ")

result = text.replace(text[0], symbol)

print(result)