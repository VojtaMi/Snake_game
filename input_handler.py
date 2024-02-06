import turtle


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
