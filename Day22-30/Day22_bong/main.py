'''mod'''
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle ((350,0))
l_paddle = Paddle ((-350,0))
ball_pos = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(ball_pos.move_speed)
    screen.update()
    ball_pos.move()

    #Detect collition with the wall
    if ball_pos.ycor() > 280 or ball_pos.ycor() < -280:
        ball_pos.bounce_y()

    #Detect collition with paddel
    if ball_pos.distance(r_paddle) < 50 and ball_pos.xcor() > 320 or ball_pos.distance(l_paddle) < 50 and ball_pos.xcor() < -320:
        ball_pos.bounce_x()

    #Detect when right paddle misses
    if ball_pos.xcor() > 380:
        ball_pos.reset_pos()
        scoreboard.l_point()

    #Detect when left paddle misses
    if ball_pos.xcor() < -380:
        ball_pos.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
