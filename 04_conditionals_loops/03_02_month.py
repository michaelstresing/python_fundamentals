'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

usernum = int(input("Please enter a number: "))

if usernum <= 12 and usernum >= 1:
    if usernum == 1:
        print("January")
    elif usernum == 2:
        print("February")
    elif usernum == 3:
        print("March")
    elif usernum == 4:
        print("April")
    elif usernum == 5:
        print("May")
    elif usernum == 6:
        print("June")
    elif usernum == 7:
        print("July")
    elif usernum == 8:
        print("August")
    elif usernum == 9:
        print("September")
    elif usernum == 10:
        print("October")
    elif usernum == 11:
        print("November")
    elif usernum == 12:
        print("December")
else:
    print("Other")
