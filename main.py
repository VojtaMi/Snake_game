import turtle
from turtle import Screen
from background import Background
from menu import MainMenu

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 660


def setup_screen():
    """
     Set up the game screen.
    :return: Screen: Initialized turtle screen.
    """
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Snake game")
    screen.tracer(0)
    return screen

if __name__ == "__main__":
    # set up the screen
    screen = setup_screen()
    # display background
    background = Background()

    # start a menu decision loop
    main_menu = MainMenu(screen)
    main_menu.make_decision()

    screen.mainloop()
