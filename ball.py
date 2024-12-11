from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.setheading(30)
        self.color('white')
        self.penup()

    def move(self):
        self.forward(10)

    def x_collision(self):
        # reflect the x axis heading
        heading = self.heading()
        new_heading = 180-heading
        self.setheading(new_heading)
        # the setheading() function handles negative coordinates

    def y_collision(self):
        # reflect the y axis heading
        heading = self.heading()
        self.setheading(360-heading)

    def reset(self):
        self.goto((0,0))