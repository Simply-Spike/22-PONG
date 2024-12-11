from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Terminal', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", align=ALIGNMENT, move=False,font=FONT)
     # function to increment score
    def add_score(self):
        self.score += 1
        self.refresh()

    # function to refresh scoreboard
    def refresh(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, move=False, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("YOU WIN!", align=ALIGNMENT, font=FONT)

    def is_winner(self,winning_score):
        if self.score>=winning_score:
            self.game_over()
            return True
        else:
            return False