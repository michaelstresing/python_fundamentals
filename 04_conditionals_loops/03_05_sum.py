'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

firstnum = int(input("Please enter the lower bound:"))
secondnum = int(input("Please enter the upper bound:"))

if firstnum > secondnum:
    print("Please keep the lower bound less than the upper bound!")

total = 0

for num in range(firstnum, secondnum):
    total += num

print(total)