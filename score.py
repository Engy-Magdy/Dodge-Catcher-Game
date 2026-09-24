from turtle import Turtle
class Score(Turtle):
    def __init__(self):
       
        super().__init__()
        self.score=0
        self.highscore=self.update_highscore()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.message()
    def message(self):
        self.write(f"Score:{self.score}",font=("courier",30,"normal"),align="center")
        self.hideturtle()
    def update_score_greenturtle(self):
        self.clear()
        self.score+=50
        self.message()
    def update_score_forms(self):
        self.clear()
        self.score+=10
        self.message()
    def update_highscore(self):
        with open("highscore.txt") as file:
            return int(file.read())
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))
