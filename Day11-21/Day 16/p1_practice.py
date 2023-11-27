'''modulefro cleaning the screen'''
import os
import p2_practice

os.system('cls')

print (p2_practice.another_modulo)


# from turtle import Turtle
# timmy = Turtle
import turtle
timmy = turtle.Turtle()

print (timmy)
timmy.shape("turtle")
timmy.color("green")

timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(150)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(50)
timmy.right(90)
timmy.forward(100)



my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
