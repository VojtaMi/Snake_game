from turtle import Screen

import menu

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 660


def setup_screen():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("#c19a6b")
    screen.title("Snake game")
    screen.tracer(0)
    return screen


# Set up the screen
screen = setup_screen()
main_menu = menu.Menu(screen)
main_menu.make_decision()

screen.exitonclick()
