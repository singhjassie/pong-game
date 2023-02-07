from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score_board import Score

game_screen = Screen()
game_screen.bgcolor("black")
game_screen.title("Pong Game")
game_screen.setup(width=800, height=600)
game_screen.tracer(0)

game_is_on=True
def pause_resume():
    global game_is_on
    if game_is_on:
        game_is_on=False
    else:
        game_is_on=True
        start_game()

game_screen.listen()
right_paddle = Paddle((380, 0))
game_screen.onkey(right_paddle.move_up, "Up")
game_screen.onkey(right_paddle.move_down, "Down")
left_paddle = Paddle((-380, 0))
game_screen.onkey(left_paddle.move_up, "w")
game_screen.onkey(left_paddle.move_down, "s")
game_screen.onkey(pause_resume, "space")


ball = Ball()
score = Score()

def start_game():
    while game_is_on:
        ball.move()
        ball.wall_collision()
        ball.paddle_collision(right_paddle.ycor(), left_paddle.ycor())
        if ball.xcor() > 405:
            score.l_score+=1
            score.update_score()
            ball.reset_position()
        elif ball.xcor() < -405:
            score.r_score+=1
            score.update_score()
            ball.reset_position()
        sleep(ball.move_speed)
        game_screen.update()


start_game()
game_screen.exitonclick()