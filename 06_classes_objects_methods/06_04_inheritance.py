'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class FootballLeague:

    def __init__(self, name='name', country='country', ucltrophies='0'):
        self.name = name
        self.country = country
        self.ucltrophies = ucltrophies

    def __str__(self):
        return f"The league, {self.name}, based in {self.country} has {self.ucltrophies} Champions League trophies."

    def printme(self):
        return f"The team, {self.name}, based in {self.country} has {self.ucltrophies} Champions League trophies."

    def winatrophy(self):
        self.ucltrophies += 1
        print(f"A team from {self.name} won! They now have {self.ucltrophies} trophies!")


class FootballTeam(FootballLeague):

    def __init__(self, name='name', city='city', leaguewins='0'):
        FootballLeague.__init__() #Seems unclear why this is needed for subclasses - as far as I could research it relates to the interpreted nature of Python?
        self.name = name
        self.city = city
        self.leaguewins = leaguewins


class Footballer(FootballTeam):

    def __init__(self, name='name', team='team', position='none', number='0'):
        FootballTeam.__init__()
        self.name = name
        FootballTeam.name = team
        self.number = number
        self.position = position

    def __str__(self):
        return f"The footballer, {self.name}, wears {self.number} playing for {self.teams}."

    def printme(self):
        return f"The footballer, {self.name}, wears {self.number} playing for {self.teams}."


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

prem = FootballLeague("English Premier League", "England", 13)

barca = FootballTeam('FC Barcelona', 'Barcelona', 5)
juve = FootballTeam('Juventus', 'Turin', 2)
liverpool = FootballTeam('Liverpool FC', 'Liverpool', 12)

thisyear = UCLWinners('Liverppol FC', 2019, "Virgil van Dijk")
twothousandtwelve = UCLWinners('Chelsea FC', 2012, "Didier Drogba")

print(ronaldo)

barca.winatrophy()

print(barca)

print(barca.ucltrophies + juve.ucltrophies)

messi.teams = "Arsenal"

print(messi)