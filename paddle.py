from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self, init_pos, heading =90):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.setheading(heading) # set turtle so that it is pointed north (up on screen)
        self.penup()
        self.shapesize(1,5)
        self.setpos(init_pos)
        

    def paddle_up(self):
        self.forward(25)

    def paddle_down(self):
        self.backward(25)
        
    def paddle_hit(self, ball):
        # is ball is inside x coordinates of paddle?
        if((ball.xcor()>=(self.xcor()-20)) and (ball.xcor()<=(self.xcor()+20))):
            #is ball inside y coordinates of paddle?
            if(ball.ycor()<=(self.ycor()+50) and ball.ycor()>=(self.ycor()-50)):
                ball.x_collision()
                return True
        return False