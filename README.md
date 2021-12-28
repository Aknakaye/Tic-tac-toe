# Tic-tac-toe
Tic-tac-toe game with minmax algorithm which is a research algorithm his objective is to find the best move to play by going through all the different scenarios.
## General info
The first message shows the player different options, the first one : if he wants to play against another player, the second one : if he wants to play against the robot, if it's the case, he must  choose a symbol (X or O).

After that the player must tap a number between 1 and 9 to choose where to put an X or O.

Different messages are displayed at the end of the game ,there is one  that shows who won (one of the players or the robot),and another showing that nobody won.

## Project files
### main.py 
Launch a Tic-tac-toe game between two player or player and robot, display the sequence of the game and the winner at the end.
### minmax.py
Contains the functions:
* minimax(board,isMax) :In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible ,every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.
* findBestMoveForO(board) : To check whether or not the current move is better than the best move we take the help of minimax() function which will consider all the possible ways the game can go and returns the best value for that move, assuming the opponent also plays optimally 
* findBestMoveForX(board) : the same operation of the function findBestMoveForO(board) the only difference it treats the case where the X will play
### tictactoe.py
Contains the functions:
* showTable(table):show tictactoe board
* winCheck(board):show tictactoe board
* endCheck(table):check if the game is end 
## Technologies
Project is created with:

* Python version : 3.10
## Setup
To run this project:
```
$ python main.py 
or 
$ py main.py
```

    
