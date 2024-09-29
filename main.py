import time
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake Game")



screen.tracer(0)
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect a dot
    if snake.head.distance(food)<15:
        food.refresh()
        score.score_update()
        snake.snake_extend()
      #detect the wall and react
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:

        score.high()
        snake.reset()
        #detecting its tail
    for square in snake.all_turtle[1:]:
        # game.all_turtle[1::]
        #  if square==game.head:
        #      pass
         if snake.head.distance(square)<10:
             score.high()
             snake.reset()










screen.exitonclick()