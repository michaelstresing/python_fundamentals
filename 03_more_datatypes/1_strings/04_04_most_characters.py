'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

sentence1 = str(input("Enter the first string: "))
sentence2 = str(input("Enter the second string: "))
sentence3 = str(input("Enter the third string: "))

if len(sentence1) > len(sentence2) and len(sentence1) > len(sentence3):
    print(sentence1)

elif len(sentence2) > len(sentence1) and len(sentence2) > len(sentence3):
    print(sentence2)

elif len(sentence3) > len(sentence1) and len(sentence3) > len(sentence2):
    print(sentence3)

elif len(sentence3) == len(sentence1) and len(sentence3) > len(sentence2):
    print(f"{sentence3} and {sentence1} are equal length, and the longest")

elif len(sentence2) == len(sentence1) and len(sentence2) > len(sentence3):
    print(f"{sentence1} and {sentence2} are equal length, and the longest")

elif len(sentence2) == len(sentence3) and len(sentence3) > len(sentence1):
    print(f"{sentence3} and {sentence2} are equal length, and the longest")

elif len(sentence2) == len(sentence3) == len(sentence1):
    print("All strings are the same length")

else:
    print ("What's happened here?!")