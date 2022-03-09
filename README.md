# games-central
A game central made while reviewing some python basics

## Code
The play.py when executed, writes in terminal requesting for an input, that, depending the number will open a game, by default the 2 games can be played:

<pre>
  -Guess the number
  -Hangsman
</pre>

## How to add more games
To add more games is simple, you just need to place a python file, that contains a master class called Game, in games directory, and import it in play.py:


File location:
<pre>
Games-central
  | play.py
  | games
      | name_of_the_game.py
</pre>
Sample to game:
<pre>
name_of_the_game.py

  class Game:
    ...
</pre>
Import to play.py:
<pre>
play.py

  from games import name_of_the_game
</pre>
