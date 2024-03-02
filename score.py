from turtle import Turtle
import utils


class Score:
    def __init__(self):
        self.score = 0
        self.pen = utils.Pen()
        self.display()

    def increase(self):
        self.score += 1

    def display(self):
        self.pen.clear()
        pos = (180, -315)
        self.pen.write_line(pos, "Score: {}".format(self.score), 15, "bold")


