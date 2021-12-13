from math import sqrt
from random import randint
from graphics import Circle, Point


color = ("red", "blue", "green", "yellow", "black", "white", "cyan", "purple")


class Asteroid:
    def __init__(self):
        self.dX = randint(-50, 50)
        self.dY = randint(-50, 50)
        self.size = randint(50, 200)
        loc = Point(200 + randint(0, 3600), 200 + randint(0, 2600))
        self.circle = Circle(loc, self.size)
        self.color = color[randint(0, 7)]
        self.circle.setFill(self.color)
        if self.color != "yellow" and self.color != "white":
            self.circle.setOutline(self.color)
