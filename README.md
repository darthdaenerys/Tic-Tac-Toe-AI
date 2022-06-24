# Intelligent AI in Tic Tac Toe

***The Tic-Tac-Toe game is also known as the “Noughts and crosses”. It is one of most widespread pen-and-paper based game for two players.***

It is mostly placed by young children, but many a time, you can also spot adults playing this to cut-off boredom. This game is quite handy and is played anywhere, with just two players. Each player has to choose one symbol between X and O. The game is played in the 3×3 grid. Each player can place only one symbol per turn and then the turn gets relayed to the other player.

## Game paradigm

- **Winning**: Each of the players tries to place their symbols in three adjacent horizontal, vertical, or diagonal cells. One who achieves this alignment earlier is the winner. While the second Player tries to interrupt Player 1’s alignment by placing his own symbols in between the symbols of Player 1.
- **Loosing**: If your competitor gets the required alignment of symbols first, you lose.
- **Draw**: If all the nine cells of the grip are marked, and none of the players, achieves the required alignment. The condition is a draw or tie. None of the players gets a point in this case. This condition takes place numerous times during the game-play and is actually amusing.

## About it

Due to its simplicity, tic-tac-toe is considered to be a perfect pedagogical tool for teaching logic-building and sportsmanship to children. Technically, there is much more to it, you can create a game tree using artificial intelligence that shows you the possibility of all combinations of the symbols and cells. If the game is played optimally by both the players, the game will end in a draw. This makes tic-tac-toe a futile game.

![](Welcome%20Screen.png)

Here, is a game of tic tac toe for a single player vs an AI, implemented using OpenCV. I have seen a lot of tic tac toe as CLI application with I/O interface and I personally never enjoyed playing as instead of just a simple mouse click you have to enter the row and column number.

![](Tic%20Tac%20Toe%20AI%201.png)

- The computer randomly assigns one of the symbols to player and other to itself.
- The player may start playing by just clicking on the cell they wish to put their symbol on.
- The game calculates scores for both and displays as a table on the side.

![](Tic%20Tac%20Toe%20AI%202.png)

- If there is a match, you'll see an animated line connecting the 3 same symbols.
- The green coloured highlighted box on the right tells which player has the move and it switches based on the turn.
- If the game is a draw, then you don't have to worry about running the program again. The computer would clean up the board for you and you're ready for another play :)
- The game also calculates scores for both the players. A ```Reset``` button is added in case you want to reset the scores.
- The scores are saved even after closing the program.
- If you're done playing, press `q` on your keyboard or the ```Quit``` button to quit.

![](Tic%20Tac%20Toe%20AI%203.png)

## Strategy

A player can play a perfect game of tic-tac-toe (to win or at least draw) if, each time it is their turn to play, they choose the first available move from the following list, as used in Newell and Simon's 1972 tic-tac-toe program.

1. Win: If the player has two in a row, they can place a third to get three in a row.
2. Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
3. Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
4. Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it. Otherwise, the player should block all forks in any way that simultaneously allows them to make two in a row. Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in them producing a fork. For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win. (Playing a corner move in this scenario produces a fork for "X" to win.)
5. Center: A player marks the center. (If it is the first move of the game, playing a corner move gives the second player more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
6. Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
7. Empty corner: The player plays in a corner square.
8. Empty side: The player plays in a middle square on any of the four sides.

**Challenge: Go ahead and try to make your first score :)**

## Tools Used

- Python v3.9.7
- Visual Studio Code
- OpenCV-Python v4.5.5
- Numpy v1.22.2