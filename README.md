# Snake Game

## Description

This project is an implementation of the traditional snake game. 
The game is written in Python 3.12 and uses turtle graphical library.


 <img src="https://github.com/VojtaMi/Snake_game/assets/146477483/d8eb0462-b13d-439d-8362-b79de1d56c8e" alt="snake game" width="400">

## How to download the game
### Prerequisites
1. Getting Python
   - You can check if Python is installed by running the following commands in your terminal (for macOS/Linux) or command prompt/PowerShell (for Windows)
   ```sh
   python --version
   ```
   - If you dont't have Python or the version is older than 3.8, you can install it from this link:   <a href="https://www.python.org/"> https://www.python.org/</a>

2. Getting Git
   - You will need Git to clone this repository. If you don't have Git installed on your computer,
     you can download it from this link: <a href="https://git-scm.com/downloads">https://git-scm.com/downloads</a>
### Game Installation
1. Clone the Repository
   Select the folder in your computer where you want the project to be saved.
   Open there the terminal window/command prompt.
   To clone the project run the following command in your terminal or command prompt:
   ```sh
   git clone https://github.com/VojtaMi/Snake_game
   ```
2. Run the game using Python
   In the same terminal window run the following command
     ```sh
   python Snake_game/main.py
   ```

## Game Description

### Menu
After opening the project the simple menu shows. 

#### To navigate use keys:
- **w** for selecting an upper option
- **s** for lower option. 
- **Enter** key is used to approve the selected option.

#### Menu options:
- **Play Game**: Runs a new snake game
- **Leaderboard**: Displays the table of the highest saved scores
- **Exit**: Terminates the program

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/1bf5fbb5-067a-4084-a3a7-128f1cc1a80a" alt="snake game menu" width="400">

### Game Mechanics
The goal of the game is to eat as many green dots as possible. 
After eating a dot the snake body gets a bit larger each time and the player's score increases. 
Sore table shows at the right down corner. 

#### To move the snake use keys:
- **w** for moving up
- **a** moving left
- **s** moving down
- **d** moving right

The game ends when the snake hits the border of the play field, colides with its body, or when it covers the whole area of the play field.

If the score qualifies to be saved in the leaderboard the promt asking for the player's name is shown. 
(The player's name is cut to 10 characters for the leaderboard table. When the player doesn't enter any name "___" is subsidized)

<img src="https://github.com/VojtaMi/Snake_game/assets/146477483/4912366e-cad0-4512-babb-b6cfc8345271" alt="snake game menu" width="400">







   
 

   
    
  
   
