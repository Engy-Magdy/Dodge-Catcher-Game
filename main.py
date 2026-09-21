from turtle import Turtle ,Screen
from paddle import Paddle
from forms import Forms
from score import Score
import time

screen=Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Dodge Catcher Game")
paddle=Paddle((0,-250))
screen.listen()
screen.onkey(paddle.right,"Right")
screen.onkey(paddle.left,"Left")
game_on=True

board_score=Score()

while game_on:
    form=Forms()
    
    time.sleep(0.1)
    while True:
        if form.distance(paddle)>40:
            form.move()
            screen.update()
            time.sleep(0.01)
        elif form.distance(paddle)<=40:
            if form.shape()=="turtle" and form.color()[0]=="white":
                message=Turtle()
                message.color("white")
                message.penup()
                message.goto(0,0)
                message.write("Game Over",font=("courier",40,"normal"),align="center")
                message.hideturtle()
                game_on=False
                screen.exitonclick()
            elif form.shape()=="turtle" and form.color()[0]=="green":
                board_score.update_score_greenturtle()
                form.hideturtle()
                break
            else:
                board_score.update_score_forms()
                form.hideturtle()
                break
        if form.ycor()<-300:
            form.hideturtle()
            break
              

    
 
