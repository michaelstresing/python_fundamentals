'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))

    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except ValueError:
        print("Please enter numbers only")
