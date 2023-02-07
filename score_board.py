from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 240)
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}\t{self.r_score}", align="center", font=("Arial", 40, "normal"))
        print("score updated")