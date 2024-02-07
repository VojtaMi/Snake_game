from turtle import Turtle
class BorderTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.fillcolor("#8AC847")
        self.pencolor("#6f4e37")

    def draw_square(self, corner):
        self.begin_fill()
        x = corner
        y = corner
        self.teleport(-x, -y)
        self.goto(x, -y)
        self.goto(x, y)
        self.goto(-x, y)
        self.goto(-x, -y)
        self.end_fill()


class Background:
    def __init__(self):
        self.border_turtle = BorderTurtle()
        # fill play field green
        self.border_turtle.draw_square(290)

