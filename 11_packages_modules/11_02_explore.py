'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''
'''
numpy *
Pandas


Django
Flask


TensorFlow
Keras

scrapy
beautifulsoup *

sqlalchemy *

'''

#'Package' is a python file with a setup.py file in it. (Can be pip installed).
#'Module' is a class or file within the package you can import.

#math datetime time (inside standard library)


import datetime

d = datetime.date(1990, 9, 9)
print(d)
#do not use the hanging 0 infront of the month or day entries

d = datetime.date.today()
print(d)

d = datetime.datetime.today()
print(d)

t = datetime.time(12, 2, 15)
print(t)

d = datetime.date.today().weekday()
print(d)
#isoweekday vs. weekday - unclear why one over other?

d = datetime.timezone.utc
print(d)

help(datetime.timezone)  #https://julien.danjou.info/python-and-timezones/

