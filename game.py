import turtle
from food import Food
from snakebody import SnakeBody, Direction
from score import Score
import utils
import time
import leaderboard

GRID_SIZE = 20


class Game:
    """
    Game logic controller.
    """
    def __init__(self):
        self.screen = turtle.Screen()
        self.snake = SnakeBody()
        self.food = Food(occupied_spots=self.snake.segments_positions())
        self.score = Score()
        self.input_handler = utils.InputHandler()

    def play(self):
        game_loop = True

        while game_loop:
            # check if snake's head and food are at the same spot, balancing float mistake
            if utils.same_grid(self.snake.head.pos(), self.food.pos()):

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

        self._end_game()

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

    def _end_game(self):
        """
        display ending animation, check for high score
        """
        time.sleep(0.5)
        self._remove_snake_from_screen()
        time.sleep(0.3)

        # display "Game Over" on screen
        self._display_game_over()

        # clear score
        self.score.pen.clear()

        # if the score is in top 5, add to the leaderboard
        leaderboard.add_if_high_score(self.score.score)

    def _display_game_over(self):
        """ Displays "Game Over" on screen for a "duration" seconds """
        duration = 1

        # writing object
        pen = utils.Pen()
        pos = (-160, -100)
        pen.write_line(pos, "Game\nover", 100)

        self.screen.update()
        time.sleep(duration)
        pen.clear()

    def _remove_snake_from_screen(self):
        self.snake.snake_animation.wipe_snake()
        self.food.hideturtle()
        self.screen.update()

