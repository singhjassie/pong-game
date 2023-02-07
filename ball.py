from turtle import Turtle
from random import randrange

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move()
        self.move_speed=0.1

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(45)

    def move(self):
        self.forward(10)

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            print("wall hitted")
            self.bounce_y()

    def paddle_collision(self, right_paddle_pos,left_paddle_pos):
        if self.xcor() > 360 and self.ycor() > right_paddle_pos - 50 and self.ycor() < right_paddle_pos + 50 :
            self.bounce_x()
        elif self.xcor() < -360 and self.ycor() > left_paddle_pos - 50 and self.ycor() < left_paddle_pos + 50 :
            self.bounce_x()
            
    def bounce_y(self):
        i = self.heading()
        self.setheading(-i)
    
    def bounce_x(self):
        i = self.heading()
        self.move_speed *= 0.9
        self.setheading(-180-i)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()