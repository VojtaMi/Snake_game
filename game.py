from food import Food
from snakebody import SnakeBody, Direction
from score import Score
import utils
from turtle import Turtle
import time
import leaderboard

GRID_SIZE = 20


class Game:
    """
    Game logic controller.
    """
    def __init__(self, screen, input_handler):
        """

        :param screen: turtle screen where game is displayed
        :param input_handler:  key listener from utils.py
        """
        self.screen = screen
        self.snake = SnakeBody()
        self.food = Food(occupied_spots=self.snake.segments_positions())
        self.score = Score()
        self.input_handler = input_handler

    def play(self):
        game_loop = True

        while game_loop:
            # check if snake's head and food are at the same spot, balancing float mistake
            if utils.check_proximity(self.snake.head.pos(), self.food.pos()):

                # when the food is eaten, the snake grows at its tail
                self.snake.pin_segment(GRID_SIZE)

                # try to place food at free spot, if no space is available, game ends
                if self.food.place(occupied_spots=self.snake.segments_positions()):
                    self.score.increase()
                    self.score.display()
                else:
                    game_loop = False

            # continue with the snake movement
            self.snake.move(GRID_SIZE, self.screen)

            if self.snake.collision():
                game_loop = False

            # checks for the flag from input_handler and sets the direction of snake's head
            self._move_on_key()

    def _move_on_key(self):
        """
        Checks for the flag from input_handler and sets the direction of snake's head
        """
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
        """
        display ending animation, check for high score
        """

        short_sleep = 0.3
        medium_sleep = 0.5
        long_sleep = 1.0

        time.sleep(medium_sleep)

        # remove all elements from the screen
        self.snake.snake_animation.wipe_snake()
        self.food.hideturtle()
        self.screen.update()

        time.sleep(short_sleep)

        # write "Game Over" on screen
        end_pen = GameOverWrite()
        self.screen.update()

        time.sleep(long_sleep)

        # clear screen
        end_pen.clear()
        self.score.pen.clear()

        # if the score is in top 5, add to the leaderboard
        leaderboard.add_if_high_score(self.score.score)


class GameOverWrite(Turtle):
    """
    Displays "Game Over" on screen.
    """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self._write_game_over()

    def _write_game_over(self):
        self.penup()
        self.goto(-160, -100)
        self.write("Game\nover", font=("Courier", 100, "normal"))
