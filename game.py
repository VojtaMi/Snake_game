from food import Food
from snakebody import SnakeBody, Direction
from score import Score
import utils
from turtle import Turtle
import time
import leaderboard


GRID_SIZE = 20


class Game:
    def __init__(self, screen, input_handler):
        self.screen = screen
        self.snake = SnakeBody()
        self.food = Food(occupied_spots=self.snake.segments_positions())
        self.score = Score()
        self.input_handler = input_handler

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
        input_key = self.input_handler.get_key_pressed()
        if input_key == "d":
            self.snake.turn(Direction.RIGHT)
        if input_key == "w":
            self.snake.turn(Direction.UP)
        if input_key == "a":
            self.snake.turn(Direction.LEFT)
        if input_key == "s":
            self.snake.turn(Direction.DOWN)


    def end_game(self):
        time.sleep(0.5)

        # remove all elements from the screen
        self.snake.snake_animation.wipe_snake()
        self.food.hideturtle()
        self.screen.update()

        time.sleep(0.3)

        end_pen = GameOverWrite()
        end_pen.write_game_over()
        self.screen.update()

        time.sleep(1)

        end_pen.clear()
        self.score.pen.clear()

        leaderboard.add_if_high_score(self.score.score)



class GameOverWrite(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def write_game_over(self):
        self.penup()
        self.goto(-160, -100)
        self.write("Game\nover", font=("Courier", 100, "normal"))