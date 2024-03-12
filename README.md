# Snake Game in Python

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#1-description">Description</a>
    </li>
    <li>
      <a href="#2-how-to-download-the-game">How to Download the Game</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#game-installation">Game Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#3-game-description">Game Description</a>
        <ul>
          <li><a href="#menu">Menu</a></li>
         <li><a href="#game-mechanics">Game Mechanics</a></li>
         <li><a href="#leaderboard">Leaderboard</a></li>
        </ul>
    </li>
    <li>
        <a href="#4-internal-implementation-comments">Internal Implementation Comments</a>
    </li>
    <li><a href="#5-license">License</a></li>
  </ol>
</details>

## 1. Description

This project is an implementation of the traditional snake game, written in Python 3.12 and utilizing the turtle graphical library.

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/d8eb0462-b13d-439d-8362-b79de1d56c8e" alt="Snake Game" width="400">


## 2. How to Download the Game

### Prerequisites

1. **Getting Python:**
   - Check if Python is installed by running the following commands in your terminal (for macOS/Linux) or command prompt/PowerShell (for Windows):
     ```sh
     python --version
     ```
   - If Python is not installed or the version is older than 3.12, you can install it from [here](https://www.python.org/).

 **Getting Git:**
   - Git is required to clone this repository. If you don't have Git installed, download it [here](https://git-scm.com/downloads).

### Game Installation

1. **Clone the Repository:**
   - Choose the folder on your computer where you want to save the project.
   - Open the terminal window/command prompt in that location.
   - Clone the project using the following command:
     ```sh
     git clone https://github.com/VojtaMi/Snake_game
     ```

2. **Run the Game using Python:**
   - In the same terminal window, run the following command:
     ```sh
     python Snake_game/main.py
     ```

## 3. Game Description

### Menu

Upon opening the project, a simple menu is displayed.

#### Navigation Keys:
- **w**: Select upper option
- **s**: Select lower option
- **Enter**: Confirm the selected option

#### Menu Options:
- **Play Game**: Start a new snake game
- **Leaderboard**: Display the table of the highest saved scores
- **Exit**: Terminate the program

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/1bf5fbb5-067a-4084-a3a7-128f1cc1a80a" alt="Snake Game Menu" width="400">

### Game Mechanics

The goal is to eat as many green dots as possible. After eating a dot, the snake's body grows, and the player's score increases. The score table is shown at the bottom-right corner.

#### Move the Snake using Keys:
- **w**: Move up
- **a**: Move left
- **s**: Move down
- **d**: Move right

The game ends when the snake hits the border, collides with its body, or covers the entire play field.

If the score qualifies for the leaderboard, a prompt for the player's name is displayed. (The player's name is limited to 10 characters for the leaderboard table. When no name is entered, "___" is used.)

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/4912366e-cad0-4512-babb-b6cfc8345271" alt="Snake Game Score Prompt" width="400">

### Leaderboard

The leaderboard stores the highest scores, with a maximum of 5 entries.

A score qualifies for the leaderboard if the table has less than 5 members or if the score is higher than the last member's score.

The leaderboard display menu has only one option: **Exit**, which returns the user to the main menu when **Enter** is pressed.

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/3e12f777-83fc-4481-99f8-31f8f1ec468f" alt="Leaderboard Menu" width="400">

## 4. Internal Implementation Comments

This project follows object-oriented principles, making some functionalities easily reusable in other programs. Notably, the Menu class from the menu.py module and the InputHandler class from utils.py can be useful in other projects.

The program generates a file named high_scores.csv in the project's folder to permanently save the leaderboard, ensuring persistence even after the program terminates.

For detailed documentation, please refer to the docstrings and code comments throughout the project.

## 5. License

Distributed under the MIT License. See `LICENSE.txt` for more information.


