# Gomuku (Swap2)
A east asian board game simular to tic-tac-toe, except it's played on a 15x15 board and you need to get 5 in a row to win.
![Image of a Go board](screenshots/Screenshot%202026-07-16%20at%2021.20.01.png)

[Play it here]()
## Quickstart
## Features
## How to run code locally
Requires Python 3.12.13 and Pygame 2.6.1 (Note that the project will still technically work inside of the newer Python versions, but on 3.14.6 specifically the music is broken). Preferably inside a virtual environment.
Clone the project from GitHub, then run main.py.

Or you can follow the Quickstart instructions above and download the game from itch.io (not there yet as of July 22th 16:39).

## How it works
Pygame creates a window and draws lines to form the game board. Circles are drawn to represent stones according to the board positions list. Clicking on a spot on the board uses math to find which spot the stone should be placed at, and together with the current turn changes the list of board positions to include the placed stone.

To figure out when the game is over, an algorithm scans the board every frame to see if there is any five-in-a-rows, and returns their position if yes in order to draw a line highlighting the winning pattern.

### For the bot, well.........

There are two reasons why the bot may make a move. 1 is that the bot needs to defend, and 2 is that the bot needs to attack. Mostly defense is prioritied above offence, except when the offence creates a threat that outweighs the current threat needing to be defended.

To find places to attack or defend, a function scans in all 8 directions for all 225 possible spots (1800 iterations in total) and compares the iterations against a specified pattern, for example [0,1,1,1,0] is an open 3 and [0,1,1,1,1,0] is impending doom (open four). If it finds a position, it will add it to a list of positions, which is returned to the analyze function to be analyzed. The analyze function eventually returns a set of coordinates that the bot will place a stone at, in around the same way that a user might place a stone.

## Credits
- [Pygame official documentation](https://www.pygame.org/docs/) was helpful in getting the project started.
- [Pytutorial](https://pytutorial.com/python-pygame-draw-line-guide/) helped with drawing lines.
- [GeeksForGeeks](https://www.geeksforgeeks.org/python/pygame-drawing-objects-and-shapes/) also helped with drawing lines.  
- Music credit to Kevin MacCleod