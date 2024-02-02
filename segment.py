from turtle import Turtle


class Direction:
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270


class Segment:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        # self.turtle.shape("square")
        # self.turtle.color("blue")
        self.turtle.hideturtle()

        self.next_segment = None
        self.previous_segment = None

    def pin(self, next_segment, grid_size):
        x, y = self.turtle.position()
        direction = self.get_heading()

        if direction == Direction.RIGHT:
            next_segment.turtle.setposition(x - grid_size, y)
        elif direction == Direction.LEFT:
            next_segment.turtle.setposition(x + grid_size, y)
        elif direction == Direction.UP:
            next_segment.turtle.setposition(x, y - grid_size)
        elif direction == Direction.DOWN:
            next_segment.turtle.setposition(x, y + grid_size)

        next_segment.set_heading(direction)
        self.next_segment = next_segment
        next_segment.previous_segment = self

    def set_heading(self, angle):
        self.turtle.setheading(angle)

    def get_heading(self):
        return self.turtle.heading()

    def move(self, grid_size):
        self.turtle.forward(grid_size)

    def pos(self):
        return self.turtle.pos()

