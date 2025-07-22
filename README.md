# rollingdice
Simple Gambling CLI Game

This is a simple Python command-line script that simulates a basic gambling interaction. The program prompts the user to "gamble" by entering ‘y’ for yes or ‘n’ for no. If the user chooses yes, the program randomly selects two numbers from 1 to 5 and displays them. If the user chooses no, the game ends politely. The program allows up to 5 invalid inputs before ending the game automatically.

Example interaction:
User inputs “y” → program outputs two random numbers, e.g. [1, 3]
User inputs invalid input like “x” → program warns about invalid input and shows how many attempts are left
User inputs “n” → program thanks the user and exits

Requirements: Python 3.x (no external libraries needed).

To run the script, use the command:
python gambling_game.py

The project contains two files: the script file gambling_game.py and this README.

This project is licensed under the MIT License. Contributions are welcome—if you want to make major changes, please open an issue first to discuss them.
