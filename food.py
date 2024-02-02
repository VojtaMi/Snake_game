import turtle
from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.color("#1F6357")

        self.place()

    def pos(self):
        return self.turtle.pos()

    def place(self):
        xcor = random.randint(-14, 14) * 20
        ycor = random.randint(-14, 14) * 20
        self.turtle.teleport(xcor, ycor)


