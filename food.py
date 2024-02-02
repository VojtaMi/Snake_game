import turtle
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#1F6357")
        self.place()

    def place(self):
        xcor = random.randint(-14, 14) * 20
        ycor = random.randint(-14, 14) * 20
        self.teleport(xcor, ycor)


