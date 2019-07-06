'''

From the previous example, move your calculation of how many seconds in a year to a python executable script.

'''

'''
Original code from first example was python executable: 

minute = 60
hour = 60 * minute
day = 24 * hour
year = 365 * day
print(year)

'''

#Python executable seconds counter, for any number of days

dayswanted = input("How many days would you like to count the seconds for? (Enter 365 for 1 year)")
dayswanted_int = int(dayswanted)
secondsinday = 60 * 24 * 60
print("There are", dayswanted_int * secondsinday, "seconds in", dayswanted_int, "days.")