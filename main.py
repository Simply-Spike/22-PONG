import time
from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_over = False
winning_score = 5
screen = Screen()
screen_width = 800
screen_height =600
screen.setup(width = screen_width, height= screen_height)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

paddle_r =Paddle((350,0))
paddle_l =Paddle((-350,0))
scoreboard_r = Scoreboard((200,200))
scoreboard_l = Scoreboard((-200,200))
ball = Ball()

screen.onkey(key="Up", fun=paddle_r.paddle_up)
screen.onkey(key="Down", fun=paddle_r.paddle_down)
screen.onkey(key="w", fun=paddle_l.paddle_up)
screen.onkey(key="s", fun=paddle_l.paddle_down)


screen.listen()

while(not game_over):
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect ball collision with top & abottom walls
    if (abs(ball.ycor()) > ((screen_height-40)/2)):
        ball.y_collision()

    #detect ball collision with paddles
    paddle_r.paddle_hit(ball)
    paddle_l.paddle_hit(ball)
    
    # detect the ball traveling past the paddle
    if(abs(ball.xcor()) > ((screen_width-20)/2) ):
        # increment score
        if ball.xcor()>0:
            scoreboard_l.add_score()
            game_over = scoreboard_l.is_winner(winning_score)
        if ball.xcor()<0:
            scoreboard_r.add_score()
            game_over = scoreboard_r.is_winner(winning_score)
        # reset the ball
        ball.reset()
        # update initial heading
        ball.x_collision()
        

screen.exitonclick()
