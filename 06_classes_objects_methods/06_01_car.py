'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car(object):

    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = int(year)
        self.speed = speed

    def __repr__(self):
        return f"You've got a {self.model} from {self.year} going {self.speed} km/h."

    def speedup(self):
        self.speed += 5


    def info(self):
        return "You've got a {self.model} from {self.year} going {self.speed}"

toy = Car("Toyota", 1994)
fer = Car("Ferrari", 2018)

print(toy, fer)

toy.speedup()

#the non dundermenthod version prints "<bound method Car.info of You've got a Toyota from 1994 going 5 km/h.>"
print(f"{toy.info}")
