'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#1) Int -> Float (explicit)

sampleint = 4
conversionfloat = float(sampleint)

print(conversionfloat)

#This is an explicit conversion (int also converts implicitly to float if there is any arithmetic operation with another float. No information would be lost.

#2) Float -> Int

samplefloat = 3.6
conversionint = int(samplefloat)

print(conversionint)

#Any values after the decimal would be lost.

#3) Floor division using a float and an int

floordivide = 10 // 7

print(floordivide)

#floor division of x // y will esssential provide the int(x / y). This will only return the quotient, all values past the decimal are lost.

#4) Inputted values multiplication.

first = float(input("Enter first number"))
second = float(input("Enter second number"))

print(first * second)

