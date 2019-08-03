'''
Write a script that demonstrates a try/except/else.

'''

while True:
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except ValueError:
        print("Please enter numbers only")
    else:
        print(result)