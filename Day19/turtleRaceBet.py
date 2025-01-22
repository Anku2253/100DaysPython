from turtle import Turtle,Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput("Make your Bet","Which turtle would win? Choose a colour : ")
colors = ["red","orange","green","purple","blue","yellow"]
yPost = [-70,-40,-10,20,50,80]
allTurtles = []

for i in range(0,6):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-200,y= yPost[i])
    allTurtles.append(tim)

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in allTurtles:

        if turtle.xcor() > 230:
            isRaceOn  = False
            winningColor = turtle.pencolor()
            if winningColor == userBet:
                print(f"You've won! The {winningColor} turtle is the winner!")

            else:
                print(f"You've lost! The {winningColor} turtle is the winner!")

        randomDist = random.randint(0,10)
        turtle.forward(randomDist)


screen.exitonclick()