'''whatever'''
import os
import turtle as t
import random

os.system('cls')

t.colormode(255)
tim = t.Turtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def set_heading_in_place():
    '''place'''
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range (10):
    for _ in range (10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    set_heading_in_place()




screen = t.Screen()
screen.exitonclick()
