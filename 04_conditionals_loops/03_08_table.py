'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
'''
for num in range(0, 50):
    if num == 9:
        print(9)
    elif num == 19:
        print(19)
    elif num == 29:
        print(29)
    elif num == 39:
        print(39)
    else:
        print(num, end=' ')

print()

#again, this feel less sohpisticated than a proper solution to the question....

for num in range(0,10):
    print(num, end=' ')

print()

for num in range(11,20):
    print(num, end=' ')

print()

for num in range(21,30):
    print(num, end=' ')

print()

for num in range(31,40):
    print(num, end=' ')

print()

for num in range(41,50):
    print(num, end=' ')

   '''
#pleased with this one...

r = 1
while r < 50:
    if (r + 1) % 10 != 0:
        print(r, end= " ")
        r += 1
    else:
        print(r)
        r += 1


