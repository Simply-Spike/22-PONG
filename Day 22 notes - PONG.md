Will be making the classic pong game.

First step is always to *break down the problem*:  Which components and pieces need to be broken down into classes 
Looking at the gameboard...
- the ball
	- position, direction, speed
	- boundaries and size
	- does it render itself on the gameboard?
- Paddles
	- position, direction, speed
	- boundaries and size info
	- are inputs handled here?
	- does it draw itself on the gameboard?
- Players
	- Scores
	- configurations
- board drawing
	- drawing the gameboard
	- drawing the scores

Steps:
1. Create the Screen
2. Create and move a paddle
3. Create another paddle
4. Create and move the ball
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses the ball to score
8. Keep Score

# Create the screen
play screen size is 800w x 600h
black background
```Python
from turtle import Screen
screen = Screen()
screen.setup(width =800, height=600)
screen.bgcolor('black')
screen.title("PONG")

screen.exitonclick()
```
