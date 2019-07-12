'''
Print out every prime number between 1 and 100.

'''
'''
for num in range(1,100):
    for i in range(1,100):
        if (num % i) == num:
            break
        else:
            print(num)
 #       if num % 2 != 0:
  #          if num % 3 != 0:
   #             if num % 5 != 0:
    #                if num % 7 != 0:
     #                   if num % 11 != 0:
'''

#set range to 2-100, as 1 isn't a prime number. (Could also have added an additional if num > 1)

for num in range(2, 100):
    for i in range(2, num // 1):
        if (num % i) == 0:
            break
    else:
        print(num)

