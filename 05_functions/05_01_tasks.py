'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

userput = int(input("Please enter a number between 1 and 1,000,000,000: "))

def divby4and7(int):
    '''
    This checks if divisible by 4 and 7
    :param int: must be a number
    :return: yes or no
    '''
    if int % 4 != 0:
        function1 = False
    elif int % 7 != 0:
        function1 = False
    else:
        function1 = True

    return(f"It's {function1}, {userput} is divisible by both 4 and 7")

def divby4or7(int):
    '''
    This checks if divisible by 4 or 7
    :param int: must be a number
    :return: yes or no
    '''
    if int % 4 == 0:
        function2 = True
    if int % 7 == 0:
        function2 = True
    else:
        function2 = False

    return(f"It's {function2}, {userput} is divisible by 4 or 7")

def divby4or7ex(int):
    '''
    This checks if divisible by 4 or 7 exclusively
    :param int: must be a number
    :return: yes or no
    '''
    if int % 4 == 0:
        if int % 7 != 0:
            function3 = True
        if int % 7 == 0:
            function3 = False

    if int % 7 == 0:
        if int % 4 != 0:
            function3 = True
        if int % 4 == 0:
            function3 = False

    return(f"It's {function3}, {userput} is divisible by 4 and 7 exclusively")

print(divby4and7(userput), "\n", divby4or7(userput), "\n", divby4or7ex(userput))
