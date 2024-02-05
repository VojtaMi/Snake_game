import turtle
from turtle import Turtle
import random


def all_positions():
    possible_positions = []
    for xcor in range(-280, 280 + 1, 20):
        for ycor in range(-280, 280 + 1, 20):
            possible_positions.append((round(xcor), round(ycor)))
    return set(possible_positions)


class Food(Turtle):
    def __init__(self, occupied_spots):
        super().__init__()
        self.shape("circle")
        self.color("#1F6357")
        self.penup()
        self.pos_options = all_positions()
        self.place(occupied_spots)

    def place(self, occupied_spots):
        occupied_spots = {(round(x), round(y)) for x, y in occupied_spots}
        remaining_options = self.pos_options - set(occupied_spots)
        coordinates = random.choice(tuple(remaining_options))
        self.goto(coordinates)
