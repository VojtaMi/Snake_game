import turtle
from turtle import Turtle

import background
import leaderboard
import utils
from game import Game


class MenuState:
    """ Bare menu option - its logic without graphics  """

    def __init__(self, description):
        self.description = description
        self.functionality = lambda: print("no linked functionality yet")


class ScreenTextElement:
    """ Text element on menu screen that doesn't have runnable functionality """
    def __init__(self, pos, text, font_size=50, font_weight="normal"):
        """
        :param pos: text position on the screen
        """
        self.pos = pos
        self.text = text
        self.font_size = font_size
        self.font_weight = font_weight

    def display(self, pen: utils.Pen):
        pen.write_line(self.pos, self.text, self.font_size, self.font_weight)


class MenuOption(MenuState):
    """ A menu state with functionalities for screen display """

    def __init__(self, description: str):
        """
        :param description: would be displayed on screen
        """
        MenuState.__init__(self, description)
        # default value,
        # is expected to be defined in the menu implementation
        self.pos = (0, 0)

    def display_as_selected(self, pen: utils.Pen, arrow):
        """ Displays option as highlighted ("bold") with an arrow pointing at it """
        pen.write_line(self.pos, self.description, font_weight="bold")
        arrow.display(self.pos)

    def display_as_normal(self, pen):
        pen.write_line(self.pos, self.description)


class Menu:
    """ General menu implementation """

    def __init__(self, *options: MenuOption):
        """
        Links options together as they are in the list
        First option would be selected by default
        Last option is considered "Exit" option
        """
        self.options = options
        # keyboard input checker
        self.input_handler = utils.InputHandler()

        # selected option - later changed by the player
        self.current_option = options[0]

        # exit option is not changed
        self.exit_option = options[-1]

        # number of menu options
        self.options_count = len(options)

        # white write turtle
        self.option_pen = utils.Pen()
        self._text_pen = utils.Pen()

        # text elements without runnable functionality
        self.text_elements: [ScreenTextElement] = []

        # points at the selected option
        self.arrow = Arrow()

    def next_option(self):
        """ Sets current selected option to the next one """
        next_index = (self._current_choice_index() + 1) % self.options_count
        self.current_option = self.options[next_index]

    def previous_option(self):
        """ Sets current selected option to the previous one """
        previous_index = (self._current_choice_index() - 1) % self.options_count
        self.current_option = self.options[previous_index]

    def make_decision(self):
        """ Navigates the menu based on the user keyboard input """

        while True:

            # read menu keyboard controls
            option = self.input_handler.get_signal()

            if option == utils.Signal.DOWN:
                self.next_option()

            elif option == utils.Signal.UP:
                self.previous_option()

            elif option == utils.Signal.ENTER:
                if self.current_option is self.exit_option:
                    self._clear_menu_screen()
                    break
                self._approve_option()

            self.display_text_elements()
            self._display_options()

    def _display_options(self):
        """ Displays the current state of the menu """
        self.option_pen.clear()
        for option in self.options:
            if option == self.current_option:
                option.display_as_selected(self.option_pen, self.arrow)
            else:
                option.display_as_normal(self.option_pen)
        turtle.update()

    def _approve_option(self):
        """ run the option's functionality """
        self.input_handler.disable()
        self._clear_menu_screen()
        self.current_option.functionality()
        self.input_handler.enable()

    def add_text_element(self, text_element: ScreenTextElement):
        """ add ScreenTextElement object that is to be displayed """
        self.text_elements.append(text_element)

    def display_text_elements(self):
        """ Displays all stored non-runnable text elements of the menu """
        for text_element in self.text_elements:
            text_element.display(self._text_pen)

    def _current_choice_index(self):
        """ returns the current option index at the option list """
        return self.options.index(self.current_option)

    def _clear_menu_screen(self):
        """ Remove all menu elements from the screen"""
        self.option_pen.clear()
        self._text_pen.clear()
        self.arrow.hideturtle()


class MainMenu(Menu):
    """ Main menu of the snake game """
    def __init__(self):
        """ Define main menu options by their description"""
        self.play_game = MenuOption("Play Game")
        self.leaderboard = MenuOption("Leaderboard")
        self.exit_game = MenuOption("Exit Game")

        # initialize menu from the defined menu options
        super().__init__(self.play_game, self.leaderboard, self.exit_game)

        # define menu options functionalities and screen locations
        self._define_options_functionalities()
        self._define_options_locations()

    def f_play_game(self):
        """ Play Game menu option functionality - runs a game"""
        Game().play()

    def f_leaderboard(self):
        """ Leaderboard menu option functionality - displays the Leaderboard as a sub-menu"""
        leaderboard_menu = LeaderboardMenu()
        leaderboard_menu.make_decision()

    def _define_options_functionalities(self):
        self.play_game.functionality = self.f_play_game
        self.leaderboard.functionality = self.f_leaderboard
        self.exit_game.functionality = None
        # exit functionality is defined in the parent (menu) class by default for the last menu option

    def _define_options_locations(self):
        """ Positions menu options on screen"""

        # left align distance
        xcor_menu = -210

        self.play_game.pos = (xcor_menu, 140)
        self.leaderboard.pos = (xcor_menu, -25)
        self.exit_game.pos = (xcor_menu, -190)


class LeaderboardMenu(Menu):
    def __init__(self):
        """Simple submenu that displays leaderboard, with "Exit" as a single menu option"""
        self.exit_leaderboard = MenuOption("Exit")
        super().__init__(self.exit_leaderboard)

        self._write_heading()
        self._write_score_table()
        self.exit_leaderboard.pos = (-95, -250)

    def _write_heading(self):
        """ Heading = "Best Scores" at the top of leaderboard screen"""
        pos_heading = (-200, 165)
        self.add_text_element(ScreenTextElement(pos_heading, "Best Scores", font_weight="bold"))

    def _write_score_table(self):
        """ Reads the score table and puts it in the menu as a ScreenTextElement object"""
        scores_str = leaderboard.score_lines()
        pos_scores = (-240, -200)
        self.add_text_element(ScreenTextElement(pos_scores, scores_str, font_size=40))


class Arrow(Turtle):
    """
    White arrow that accompanies the highlighted option
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

    def display(self, pos):
        # shifts the arrow relative to the position of the highlighted text
        xcor = pos[0] - 10
        ycor = pos[1] + 40
        self.goto(xcor, ycor)

        self.showturtle()
