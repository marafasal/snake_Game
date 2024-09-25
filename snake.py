from turtle import Turtle
X_POSITION=[(0,0),(-20,0),(-40,0)]
MOV=20
DOWN=270
UP=90
LEFT=180
RIGHT=0
class Game:
    def __init__(self):
        self.all_turtle=[]
        self.join_fes()
        self.head=self.all_turtle[0]



    def join_fes(self):
        for japs in X_POSITION:
            self.extend(japs)


    def extend(self,japs):
        tom = Turtle(shape="square")
        tom.penup()
        tom.color("white")
        tom.goto(japs)
        self.all_turtle.append(tom)
    def snake_extend(self):
        self.extend(self.all_turtle[-1].position())

    def move(self):
        for tor in range(len(self.all_turtle) - 1, 0, -1):
            tor_x = self.all_turtle[tor - 1].xcor()
            tor_y = self.all_turtle[tor - 1].ycor()
            self.all_turtle[tor].goto(tor_x, tor_y)
        self.head.forward(MOV)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

