'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
#get the input, convert into a list of numbers, print to check
listinput = input('Please provide 10 numbers, separated by a space: ')
nlist = listinput.split()
nlist = [int(num) for num in nlist]
print(nlist)


sort_list = nlist[1::2] + nlist[8::-2]

print(sort_list)
