from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreBoard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()  

    #Detect colison with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    #Detect collison
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameIsOn = False
        scoreboard.gameOver()

    #detect collison with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            gameIsOn = False
            scoreboard.gameOver()


screen.exitonclick()