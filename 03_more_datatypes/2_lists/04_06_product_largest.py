'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

listinput = input('Please provide 10 numbers, separated by a space: ')

nlist = listinput.split()

#https://stackoverflow.com/questions/3371269/call-int-function-on-every-list-element
nlist = [int(x) for x in nlist]

nlist.sort()
print(f"The largest number was {nlist[9]}")

#Challenge

sum = 1
for n in nlist:
    sum *= n

print(f"{sum} is the product of all numbers")
