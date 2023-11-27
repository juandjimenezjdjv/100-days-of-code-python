'''mod'''
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collition with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            GAME_IS_ON = False
            scoreboard.game_over()

    #Detect a succeful crossing
    if player.is_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
