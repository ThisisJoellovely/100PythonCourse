import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Global Variables
level = 0
game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(level)


screen.listen()
screen.onkey(player.move , "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars(20 + (5 * level))

    # If the player has reached the other side of the road then increase the level
    if player.ycor() > 280:
        level += 1
        scoreboard.update_scoreboard(level)
        player.goto(0, -280)

    # If the player has hit a car then the game is over
    for i in range(len(car_manager.random_cars)):
        if car_manager.random_cars[i].distance(player) < 10:
            scoreboard.gameover()
            game_is_on = False

    car_manager.moving_cars(level=level)

screen.exitonclick()
