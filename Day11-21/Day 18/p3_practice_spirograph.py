'''Whatever'''
import os
from turtle import Screen
import random
import turtle as t

os.system('cls')

tim = t.Turtle()
tim.color("green")
tim.speed("fastest")

t.colormode(255)

def random_color():
    '''Doc string'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rndm_clr = (r, g ,b)
    return rndm_clr

def draw_gap(gap):
    for _ in range(int(360/gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + gap)
        tim.color(random_color())

draw_gap(5)




screen = Screen()
screen.exitonclick()
