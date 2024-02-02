from turtle import Turtle


class Direction:
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270


class Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.next_segment = None
        self.previous_segment = None

    def pin(self, next_segment, grid_size):
        next_segment.setheading(self.heading())
        next_segment.setpos(self.pos())
        next_segment.back(grid_size)

        self.next_segment = next_segment
        next_segment.previous_segment = self

