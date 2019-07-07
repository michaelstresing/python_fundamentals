'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
invamount = float(input("Please enter your investment amount (in GBP):"))
Intrate = float(input("Please enter the interest rate, as a percentage:")) / 100
Invyears = float(input("Please enter the number of years for the investment"))

#Note - formulat for investment was found here, assumed that compounded annually - https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php

print("The future value of your investment will be:", round((invamount * (1 + Intrate) ** Invyears),2), "GBP")