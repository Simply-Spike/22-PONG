import time
from turtle import Turtle, Screen
import random
from paddle import Paddle


screen = Screen()
screen.setup(width =800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

paddle_r =Paddle((350,0))
paddle_l =Paddle((-350,0))
screen.tracer(1)

screen.onkey(key="Up", fun=paddle_r.paddle_up)
screen.onkey(key="Down", fun=paddle_r.paddle_down)
screen.onkey(key="w", fun=paddle_l.paddle_up)
screen.onkey(key="s", fun=paddle_l.paddle_down)

#paddle.teleport(paddle_init_pos) # teleport added in 3.12
screen.listen()



screen.exitonclick()
