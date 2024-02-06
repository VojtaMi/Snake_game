import turtle
import game
from utils import InputHandler


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.input_handler = InputHandler()
        self.current_state = self._initialize_states()
        self.menu_enabled = True

    def _initialize_states(self):
        play_game = State("Play Game")
        leader_board = State("Leaderboard")
        exit_game = State("Exit Game")

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
        print(f"Current state: {self.current_state.description}")

    def _select_previous_state(self):
        if not self.menu_enabled:
            return
        self.current_state = self.current_state.previous
        print(f"Current state: {self.current_state.description}")

    def _approve_option(self):
        if not self.menu_enabled:
            return
        if self.current_state.description == "Play Game":
            self.menu_enabled = False  # Disable menu input
            current_game = game.Game(self.screen, self.input_handler)
            current_game.play()
            current_game.end_game()
            self.menu_enabled = True  # Re-enable menu input after the game

        elif self.current_state.description == "Exit Game":
            self.screen.bye()

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


class State:
    def __init__(self, description):
        self.next = None
        self.previous = None
        self.description = description
