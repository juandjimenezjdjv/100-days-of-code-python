'''method'''
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    '''class'''
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        '''function'''
        self.write(f"Score: {self.score} ", align=ALIGMENT, font=FONT)

    def game_over(self):
        '''function'''
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        '''function'''
        self.score += 1
        self.clear()
        self.update_score()
