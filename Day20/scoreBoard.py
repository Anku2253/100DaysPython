from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        
    def updateScore(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over! Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()
