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


class Footballer:

    def __init__(self, name='name', teams='team', number='0'):
        self.name = name
        self.teams = teams
        self.number = number

    def __str__(self):
        return f"The footballer, {self.name}, wears {self.number} playing for {self.teams}."

    def printme(self):
        return f"The footballer, {self.name}, wears {self.number} playing for {self.teams}."


class FootballClub:

    def __init__(self, name='name', city='city', ucltrophies='0'):
        self.name = name
        self.city = city
        self.ucltrophies = ucltrophies

    def __str__(self):
        return f"The team, {self.name}, based in {self.city} has won the Champions League {self.ucltrophies} time(s)."

    def printme(self):
        return f"The team, {self.name}, based in {self.city} has won the Champions League {self.ucltrophies} time(s)."

    def winatrophy(self):
        self.ucltrophies += 1
        print(f"{self.name} won! They now have {self.ucltrophies} trophies!")

    def __add__(self, otherclub):
        return FootballClub(self.ucltrophies + otherclub.ucltrophies)


class UCLWinners:

    def __init__(self, team='team', year='0000', motm='name'):
        self.team = team
        self.year = year
        self.motm = motm

    def __str__(self):
        return f"{self.motm} was Man of the Match, when {self.team} won the Champions League in {self.year}."

    def printme(self):
        return f"{self.motm} was Man of the Match, when {self.team} won the Champions League in {self.year}."


ronaldo = Footballer('Chistiano Ronaldo', 'Juventus', 7)
messi = Footballer('Leo Messi', 'Barcelona', 10)

barca = FootballClub('FC Barcelona', 'Barcelona', 5)
juve = FootballClub('Juventus', 'Turin', 2)

thisyear = UCLWinners('Liverppol FC', 2019, "Virgil van Dijk")
twothousandtwelve = UCLWinners('Chelsea FC', 2012, "Didier Drogba")

print(ronaldo)

barca.winatrophy()

print(barca)

print(barca.ucltrophies + juve.ucltrophies)

messi.teams = "Arsenal"

print(messi)