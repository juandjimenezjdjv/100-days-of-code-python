'''Module of imports'''
import os
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

os.system('cls')
def move_fowards():
    '''function'''
    tim.forward(10)
def move_backwards():
    '''function'''
    tim.backward(10)
def move_left():
    '''function'''
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    '''function'''
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    '''function'''
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
