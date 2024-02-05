from turtle import Turtle, Screen
from snakebody import SnakeBody, Direction
from food import Food
from score import Score
import utils

# Constants
GRID_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 660


def setup_screen():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("#c19a6b")
    screen.title("Snake game")
    screen.tracer(0)
    return screen


def draw_square(border_turtle, corner):
    x = corner
    y = corner
    border_turtle.teleport(-x, -y)
    border_turtle.goto(x, -y)
    border_turtle.goto(x, y)
    border_turtle.goto(-x, y)
    border_turtle.goto(-x, -y)


def paint_play_field():
    # initialize colours
    border_turtle = Turtle()
    border_turtle.hideturtle()
    border_turtle.fillcolor("#8AC847")
    border_turtle.pencolor("#6f4e37")

    # fill play field green
    border_turtle.begin_fill()
    draw_square(border_turtle, corner=290)
    border_turtle.end_fill()


# Set up the screen
screen = setup_screen()
paint_play_field()

# Initialize the snake
snake = SnakeBody()
food = Food(occupied_spots=snake.segments_positions())
score = Score()


# Game loop
game_loop = True
while game_loop:
    if utils.check_proximity(snake.head.pos(), food.pos()):
        snake.pin_segment(GRID_SIZE)
        food.place(occupied_spots=snake.segments_positions())
        score.increase()
        score.display()

    snake.move(GRID_SIZE, screen)
    if snake.collision():
        game_loop = False
    screen.listen()
    screen.onkey(lambda: snake.turn(Direction.RIGHT), "d")
    screen.onkey(lambda: snake.turn(Direction.LEFT), "a")
    screen.onkey(lambda: snake.turn(Direction.UP), "w")
    screen.onkey(lambda: snake.turn(Direction.DOWN), "s")
screen.exitonclick()
