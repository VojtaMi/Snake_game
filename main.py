from turtle import Turtle, Screen
from snakebody import SnakeBody, Direction
from food import Food
import math


def is_close(pos1, pos2):
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    return dist_x < 1 and dist_y < 1


# Constants
GRID_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Set up the screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("#8AC847")
screen.title("Snake game")
screen.tracer(0)
# paint_background()


# Initialize the snake
snake = SnakeBody()
food = Food()

snake.pin_segment(GRID_SIZE)

# Game loop
while True:
    if is_close(snake.head.pos(), food.pos()):
        snake.pin_segment(GRID_SIZE)
        food.place()
    snake.move(GRID_SIZE, screen)
    screen.listen()
    screen.onkey(lambda: snake.turn(Direction.RIGHT), "d")
    screen.onkey(lambda: snake.turn(Direction.LEFT), "a")
    screen.onkey(lambda: snake.turn(Direction.UP), "w")
    screen.onkey(lambda: snake.turn(Direction.DOWN), "s")
