from turtle import Turtle
GAME="GAME OVER"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.penup()
        self.goto(x=0,y=270)
        self.color("white")
        self.update()
        self.hideturtle()
    def update(self):
        self.clear()
        self.write(f"Score:{self.score} HighScore: {self.highscore}",align="center", font=("Arial",12,"normal"))
    # def update_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Score:{GAME}", align="center", font=("Arial", 12, "normal"))
    def high(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0

    def score_update(self):
        self.score += 1

        self.update()
