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


class InputHandler:
    """ Handles user keyboard input"""
    def __init__(self):
        self.key_pressed = None
        self.enabled = True

        turtle.listen()

        turtle.onkeypress(self.set_w_key_pressed, "w")
        turtle.onkeypress(self.set_s_key_pressed, "s")
        turtle.onkeypress(self.set_a_key_pressed, "a")
        turtle.onkeypress(self.set_d_key_pressed, "d")
        turtle.onkeypress(self.set_return_key_pressed, "Return")

    def set_w_key_pressed(self):
        self.key_pressed = "w"

    def set_s_key_pressed(self):
        self.key_pressed = "s"

    def set_a_key_pressed(self):
        self.key_pressed = "a"

    def set_d_key_pressed(self):
        self.key_pressed = "d"

    def set_return_key_pressed(self):
        self.key_pressed = "Return"

    def disable(self):
        """ When disabled Input handler doesn't return keys pressed"""
        self.enabled = False

    def enable(self):
        """ Refreshing the object"""
        self.__init__()

    def get_key_pressed(self):
        """ If enabled return the last pressed key"""
        if not self.enabled:
            return

        key = self.key_pressed
        self.key_pressed = None
        return key


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



