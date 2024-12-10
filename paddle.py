from turtle import Turtle

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
        self.forward(20)

    def paddle_down(self):
        self.backward(20)
        