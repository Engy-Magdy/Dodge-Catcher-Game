from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(1,5)
    def right(self):
        self.goto(self.xcor()+60,self.ycor())
    def left (self):
        self.goto(self.xcor()-60,self.ycor())
