from turtle import Screen
import game

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
current_game = game.Game(screen)
current_game.play()
current_game.end_game()
screen.exitonclick()
