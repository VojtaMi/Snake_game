import turtle
from turtle import Turtle

# Constants
BACKGROUND_CORNER = 290


class BorderTurtle(Turtle):
    def __init__(self):
        """Initialize the border turtle"""
        super().__init__()
        self.hideturtle()

        # green field
        self.fillcolor("#8AC847")

        # brown borderline
        self.pencolor("#6f4e37")

    def draw_square(self, corner):
        """
        Draw a filled square given corner coordinates

        Args:
        corner (int): positive number, sets xcor and ycor for corner points

        """
        self.begin_fill()
        x = corner
        y = corner

        # left down corner - initial position
        self.teleport(-x, -y)

        # right down corner
        self.goto(x, -y)

        # right up corner
        self.goto(x, y)

        # left up corner
        self.goto(-x, y)

        # left down corner - square is closed
        self.goto(-x, -y)
        self.end_fill()


class Background:
    def __init__(self):
        # make background light brown
        turtle.bgcolor("#c19a6b")

        # fill play field green
        self.border_turtle = BorderTurtle()
        self.border_turtle.draw_square(BACKGROUND_CORNER)

