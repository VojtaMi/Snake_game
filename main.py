from turtle import Turtle, Screen
from snakebody import SnakeBody, Direction
from food import Food
from score import Score


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
food = Food()
score = Score()


# Game loop
while True:
    if is_close(snake.head.pos(), food.pos()):
        snake.pin_segment(GRID_SIZE)
        food.place()
        score.increase()
        score.display()

    snake.move(GRID_SIZE, screen)
    screen.listen()
    screen.onkey(lambda: snake.turn(Direction.RIGHT), "d")
    screen.onkey(lambda: snake.turn(Direction.LEFT), "a")
    screen.onkey(lambda: snake.turn(Direction.UP), "w")
    screen.onkey(lambda: snake.turn(Direction.DOWN), "s")
