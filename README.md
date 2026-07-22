# Gomuku (Swap2)
A east asian board game simular to tic-tac-toe, except it's played on a 15x15 board and you need to get 5 in a row to win.
![Image of a Go board](screenshots/Screenshot%202026-07-16%20at%2021.20.01.png)

[Play it here]()
## Quickstart
## Features
## How to run code locally
Requires Python 3.14.6 and Pygame 2.6.1. Preferably inside a virtual environment.
Clone the project from GitHub, then run board.py.

Or you can follow the Quickstart instructions above and download the game from itch.io (not there yet as of July 16th 16:39).

## How it works
Pygame creates a window and draws lines to form the game board. Circles are drawn to represent stones according to the board positions list. Clicking on a spot on the board uses math to find which spot the stone should be placed at, and together with the current turn changes the list of board positions to include the placed stone.

## Credits
- [Pygame official documentation](https://www.pygame.org/docs/) was helpful in getting the project started.
- [Pytutorial](https://pytutorial.com/python-pygame-draw-line-guide/) helped with drawing lines.
- [GeeksForGeeks](https://www.geeksforgeeks.org/python/pygame-drawing-objects-and-shapes/) also helped with drawing lines.  
- Music credit to Kevin MacCleod