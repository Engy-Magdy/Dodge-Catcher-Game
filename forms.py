from turtle import Turtle,Screen
import random
shape=["circle","triangle","turtle","square"]
color=["green","DeepPink","white","cyan","purple"]

class Forms(Turtle):
            def __init__(self):
                      super().__init__()
                      self.shape(random.choice(shape))
                      self.color(random.choice(color))
                      self.penup()
                      self.goto(random.randint(-380,380),400)
                    
                      
                      
            def move(self):
                    self.goto(self.xcor(),self.ycor()-5)
                      
