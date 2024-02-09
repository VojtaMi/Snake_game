import turtle
from turtle import Turtle
import game
from utils import InputHandler
import leaderboard

PLAY_GAME_STR = "Play Game"
LEADERBOARD_STR = "Leaderboard"
EXIT_GAME_STR = "Exit Game"

XCOR_MENU = -210


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.input_handler = InputHandler()
        self.current_state = self._initialize_states()
        self.menu_enabled = True

        self.draw_play_game_turtle = DrawLineTurtle(PLAY_GAME_STR)
        self.draw_leaderboard_turtle = DrawLineTurtle(LEADERBOARD_STR)
        self.draw_exit_game_turtle = DrawLineTurtle(EXIT_GAME_STR)
        self.arrow = Arrow()

        self._display()

    def _initialize_states(self):
        play_game = State(PLAY_GAME_STR)
        leader_board = State(LEADERBOARD_STR)
        exit_game = State(EXIT_GAME_STR)

        play_game.next = leader_board
        leader_board.next = exit_game
        exit_game.next = play_game

        play_game.previous = exit_game
        leader_board.previous = play_game
        exit_game.previous = leader_board

        return play_game

    def _select_next_state(self):
        if not self.menu_enabled:
            return
        self.current_state = self.current_state.next
        self._display()

    def _select_previous_state(self):
        if not self.menu_enabled:
            return
        self.current_state = self.current_state.previous
        self._display()

    def _approve_option(self):
        self.clear_screen()
        self.arrow.hideturtle()

        if not self.menu_enabled:
            return
        if self.current_state.description == PLAY_GAME_STR:
            self.menu_enabled = False  # Disable menu input
            current_game = game.Game(self.screen, self.input_handler)
            current_game.play()
            current_game.end_game()
            self.menu_enabled = True  # Re-enable menu input after the game
            self._reactivate_input_handler()

        elif self.current_state.description == LEADERBOARD_STR:
            display_leaderboard(self.input_handler, self.screen)

        elif self.current_state.description == EXIT_GAME_STR:
            self.screen.bye()
            exit()

        self._display()

    def make_decision(self):

        while True:
            option = self.input_handler.get_key_pressed()
            if option == "w":
                self._select_previous_state()
            elif option == "s":
                self._select_next_state()
            elif option == "Return":
                self._approve_option()
            turtle.update()

    def _display(self):

        if self.current_state.description == PLAY_GAME_STR:
            self._display_play_game_option("bold")
        else:
            self._display_play_game_option("normal")

        if self.current_state.description == LEADERBOARD_STR:
            self._display_leaderboard_option("bold")
        else:
            self._display_leaderboard_option("normal")

        if self.current_state.description == EXIT_GAME_STR:
            self._display_exit_game_option("bold")
        else:
            self._display_exit_game_option("normal")

        self.screen.update()

    def _display_play_game_option(self, font_weight):
        pos = (XCOR_MENU, 140)
        self.draw_play_game_turtle.write_line(pos, font_weight)
        self._move_arrow_if_bold(font_weight, pos)

    def _display_leaderboard_option(self, font_weight):
        pos = (XCOR_MENU, -25)
        self.draw_leaderboard_turtle.write_line(pos, font_weight)
        self._move_arrow_if_bold(font_weight, pos)

    def _display_exit_game_option(self, font_weight):
        pos = (XCOR_MENU, -190)
        self.draw_exit_game_turtle.write_line(pos, font_weight)
        self._move_arrow_if_bold(font_weight, pos)

    def _move_arrow_if_bold(self, font_weight, pos):
        if font_weight == "bold":
            self.arrow.display(pos)

    def clear_screen(self):
        self.draw_play_game_turtle.clear()
        self.draw_leaderboard_turtle.clear()
        self.draw_exit_game_turtle.clear()

    def _reactivate_input_handler(self):
        self.input_handler = InputHandler()


class State:
    def __init__(self, description):
        self.next = None
        self.previous = None
        self.description = description


class DrawLineTurtle(Turtle):
    def __init__(self, text):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.font_size = 50
        self.text = text

    def write_line(self, start_pos, font_weight):
        self.clear()
        self.penup()
        self.goto(start_pos)
        self.write(self.text, font=("Courier", self.font_size, font_weight))


class Arrow(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def display(self, pos):
        xcor = pos[0] - 10
        ycor = pos[1] + 40
        self.goto(xcor, ycor)
        self.showturtle()


def display_leaderboard(input_handler, screen):
    scores_str = leaderboard.score_lines()
    draw_scores = DrawLineTurtle(scores_str)
    draw_scores.font_size = "40"

    pos_heading = (-200, 165)
    draw_heading = DrawLineTurtle("Best Scores")
    draw_heading.write_line(pos_heading, "bold")

    pos_scores = (-240, -200)
    draw_scores.write_line(pos_scores, "normal")

    pos_exit = (-95, -250)
    draw_exit = DrawLineTurtle("Exit")
    draw_exit.write_line(pos_exit, "bold")

    arrow = Arrow()
    arrow.display(pos_exit)

    screen.update()

    while True:
        if input_handler.get_key_pressed() == "Return":
            arrow.hideturtle()
            draw_exit.clear()
            draw_scores.clear()
            draw_heading.clear()
            return
        screen.update()
