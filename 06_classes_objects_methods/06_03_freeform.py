'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Footballer(object):

    def __init__(self, name, team, number):
        self.name = name
        self.team = team
        self.number = number


class FootballClub(object):

    def __init__(self, name, city, ucltrophies):
        self.name = name
        self.city = city
        self.ucltrophies = ucltrophies


class UCLWinners(object):

    def __init__(self, team, year, motm):
        self.team = team
        self.year = year
        self.motm = motm
