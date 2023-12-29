from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")

# Global Variables
game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.right,"Right")
s.onkey(snake.left,"Left")

while game_is_on:    
    s.update()
    time.sleep(0.1)
    snake.move_forward() 
    
    # Detect colision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail.
    for segment in snake.snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



        

    

    










s.exitonclick()
