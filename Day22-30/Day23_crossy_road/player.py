'''mod'''
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    '''class'''
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        '''method'''
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        '''method'''
        self.goto(STARTING_POSITION)

    def is_finish_line(self):
        '''method'''
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
