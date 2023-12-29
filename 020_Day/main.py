from turtle import Screen, Turtle
from snake import Snake
import time

s = Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")

# Global Variables
game_is_on = True
snake = Snake()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.right,"Right")
s.onkey(snake.left,"Left")

while game_is_on:    
    s.update()
    time.sleep(0.1)
    snake.move_forward() 
    
    

    










s.exitonclick()
