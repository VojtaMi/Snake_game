from food import Food
from snakebody import SnakeBody, Direction
from score import Score
import utils
from turtle import Turtle

GRID_SIZE = 20


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = SnakeBody()
        self.food = Food(occupied_spots=self.snake.segments_positions())
        self.score = Score()
        self.background = Background()
        self.background.paint_play_field()

    def play(self):
        game_loop = True

        while game_loop:
            if utils.check_proximity(self.snake.head.pos(), self.food.pos()):
                self.snake.pin_segment(GRID_SIZE)
                self.food.place(occupied_spots=self.snake.segments_positions())
                self.score.increase()
                self.score.display()

            self.snake.move(GRID_SIZE, self.screen)
            if self.snake.collision():
                game_loop = False
            self._move_on_key()

    def _move_on_key(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.snake.turn(Direction.RIGHT), "d")
        self.screen.onkey(lambda: self.snake.turn(Direction.LEFT), "a")
        self.screen.onkey(lambda: self.snake.turn(Direction.UP), "w")
        self.screen.onkey(lambda: self.snake.turn(Direction.DOWN), "s")


class BorderTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.fillcolor("#8AC847")
        self.pencolor("#6f4e37")

    def draw_square(self, corner):
        self.begin_fill()
        x = corner
        y = corner
        self.teleport(-x, -y)
        self.goto(x, -y)
        self.goto(x, y)
        self.goto(-x, y)
        self.goto(-x, -y)
        self.end_fill()


class Background:
    def __init__(self):
        self.border_turtle = BorderTurtle()

    def paint_play_field(self):
        # fill play field green
        self.border_turtle.draw_square(290)



