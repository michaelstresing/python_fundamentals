'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

usernum = int(input("Please enter a number between 1 and 1,000,000,000: "))

if usernum % 3 == 0:
    print ("That's divisible by 3!")

else:
    print("That's not divisible by 3")

