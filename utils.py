import turtle


def check_proximity(pos1, pos2):
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    return dist_x < 1 and dist_y < 1


class InputHandler:
    def __init__(self):
        self.key_pressed = None

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

    def get_key_pressed(self):
        key = self.key_pressed
        self.key_pressed = None
        return key
