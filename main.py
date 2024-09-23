import time
from turtle import  Screen
from snake import Game
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake Game")



screen.tracer(0)
game=Game()
food=Food()
score=Score()

screen.listen()
screen.onkey(game.up,"Up")
screen.onkey(game.down,"Down")
screen.onkey(game.right,"Right")
screen.onkey(game.left,"Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    game.move()
    #detect a dot
    if game.head.distance(food)<15:
        food.refresh()
        score.score_update()
    if game.head.xcor()>280 or game.head.xcor()<-280 or game.head.ycor()>280 or game.head.ycor<-280:
        game_on=False








screen.exitonclick()