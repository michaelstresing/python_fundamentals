'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

#option 1

sentence = input("Please enter a sentence:")

result = (sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u") + sentence.count("A") + sentence.count("E") + sentence.count("I") + sentence.count("O") + sentence.count("U"))

print(f"There are {result} vowels in your sentence")

#option 2

from collections import Counter
sentence2 = input("Please enter a sentence:")

c = Counter(sentence2)
result2 = c["a"] + c["e"] + c["i"] + c["o"] + c["u"] + c["A"] + c["E"] + c["I"] + c["O"] + c["U"]

print(f"There are {result2} vowels in your sentence")