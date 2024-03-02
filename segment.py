from turtle import Turtle


class Direction:
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270


class Segment(Turtle):
    """ Representing one segment of the snake body"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.next_segment = None
        self.previous_segment = None

    def pin(self, next_segment, grid_size):
        """ pins a new segment behind"""

        # pinned segment faces the same direction
        next_segment.setheading(self.heading())

        # screen position of pinned segment is one grid behind
        next_segment.setpos(self.pos())
        next_segment.back(grid_size)

        # linking segments together
        self.next_segment = next_segment
        next_segment.previous_segment = self

