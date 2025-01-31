from turtle import Turtle


Starting_Position = [(0,0),(-20,0),(-40,0)]
Move = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in Starting_Position:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def addSegment(self,position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for segNum in range(len(self.segments)-1,0,-1):
            newX = self.segments[segNum-1].xcor()
            newY = self.segments[segNum-1].ycor()
            self.segments[segNum].goto(newX,newY)
        self.head.forward(Move) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
