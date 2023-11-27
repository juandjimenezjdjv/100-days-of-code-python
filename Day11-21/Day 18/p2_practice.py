'''Whatever'''
import os
from turtle import Screen
import random
import turtle as t

os.system('cls')
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("blue")

t.colormode(255)

def random_color():
    '''Doc string'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rndm_clr = (r, g ,b)
    return rndm_clr

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random_color())
    timmy.speed("fastest")
    timmy.pensize(5)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
