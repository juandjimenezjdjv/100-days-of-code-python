'''pa que no moleste'''
import os
from turtle import Turtle, Screen
import random

os.system('cls')

timmy = Turtle()

timmy.shape("turtle")
timmy.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    '''lol'''
    angle = 360 / num_sides
    for _ in range (num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shapes_side_n in range (3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shapes_side_n)

screen = Screen()
screen.exitonclick()
