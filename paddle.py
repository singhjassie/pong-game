from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos_coords):
        super().__init__()
        self.pos_coords=pos_coords
        self.create_paddle()
        
    def move_up(self):
        if self.ycor() < 240:
            self.setheading(90)
            self.forward(20)


    def move_down(self):
        if self.ycor() > -240:
            self.setheading(270)
            self.forward(20)

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(self.pos_coords)