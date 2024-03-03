import turtle
from turtle import Turtle


def same_grid(pos1, pos2):
    """ Checks if two game objects are at the same grid neglecting float mistake"""
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    return dist_x < 1 and dist_y < 1

class Signal:
    """ Grouping keyboard signals by their action """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    ENTER = 4

class InputHandler:
    """ Handles user keyboard input"""
    def __init__(self):
        self.signal = None
        self.enabled = True

        turtle.listen()

        turtle.onkeypress(self.set_up, "w")
        turtle.onkeypress(self.set_down, "s")
        turtle.onkeypress(self.set_left, "a")
        turtle.onkeypress(self.set_right, "d")
        turtle.onkeypress(self.set_enter, "Return")

        turtle.onkeypress(self.set_up, "Up")
        turtle.onkeypress(self.set_down, "Down")
        turtle.onkeypress(self.set_left, "Left")
        turtle.onkeypress(self.set_right, "Right")

    def set_up(self):
        self.signal = Signal.UP

    def set_down(self):
        self.signal = Signal.DOWN

    def set_left(self):
        self.signal = Signal.LEFT

    def set_right(self):
        self.signal = Signal.RIGHT

    def set_enter(self):
        self.signal = Signal.ENTER

    def disable(self):
        """ When disabled Input handler doesn't return keys pressed"""
        self.enabled = False

    def enable(self):
        """ Refreshing the object"""
        self.__init__()

    def get_signal(self):
        """ If enabled return the signal from the last pressed key"""
        if not self.enabled:
            return

        signal = self.signal
        self.signal = None
        return signal


class Pen(Turtle):
    """
    Used to display white text on screen
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

    def write_line(self, line_pos, text, font_size=50, font_weight="normal"):
        """
        :param line_pos: where the text starts
        :param text: string to be displayed
        :param font_size: default 50
        :param font_weight: default "normal", set to "bold" for highlighted option
        """
        self.goto(line_pos)
        self.write(text, font=("Courier", font_size, font_weight))



