import turtle
from turtle import Turtle
import random
from typing import Tuple, List, Set


def all_positions() -> Set[Tuple[int, int]]:
    """
    Generate all possible positions on the game grid.

    Returns:
        set: Set of tuples representing all possible positions.
    """
    possible_positions = []
    for xcor in range(-280, 280 + 1, 20):
        for ycor in range(-280, 280 + 1, 20):
            possible_positions.append((round(xcor), round(ycor)))
    return set(possible_positions)


class Food(Turtle):
    """A class representing a food particle."""

    def __init__(self, occupied_spots: List[Tuple[float, float]]):
        """
        Initializes a Food object.
        :param occupied_spots (List[Tuple[float, float]]): List of tuples representing currently occupied spots.
        """
        super().__init__()

        # Dark green circle
        self.shape("circle")
        self.color("#1F6357")

        # Turtle doesn't write anything, it only displays itself
        self.penup()

        self.all_positions = all_positions()
        self.place(occupied_spots)

    def place(self, occupied_spots: List[Tuple[float, float]]) -> bool:
        """
        Place the food on a valid, unoccupied spot.

        :param occupied_spots: List of tuples representing currently occupied spots.
        :return: bool: True if the food was placed successfully, False otherwise.
        """

        # Round the float input so the positions are comparable
        occupied_spots = {(round(x), round(y)) for x, y in occupied_spots}

        # Set of positions where the Food can be placed
        remaining_options = self.all_positions - set(occupied_spots)

        # return False if there is no space to put the food
        if not remaining_options:
            return False

        # Random free position
        coordinates = random.choice(tuple(remaining_options))

        # Placing Food at the free spot
        self.goto(coordinates)

        # return True if placement of food was successful
        return True
