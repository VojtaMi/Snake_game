from turtle import Turtle, Screen
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(180, -315)
        self.pencolor("white")
        self.hideturtle()


class Score:
    def __init__(self):
        self.score = 0
        self.pen = Pen()
        self.display()

    def increase(self):
        self.score += 1

    def display(self):
        self.pen.clear()
        pen = self.pen
        pen.write("Score: {}".format(self.score), font=("Courier", 15, "bold"))

