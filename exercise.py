import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.speed("fastest")
my_screen = Screen()

# Making an Etch-A-Sketch App
# TODO 1: Make all the functions that will implement a move then create a higher order function for better control and readability

def tim_move_forwards():
    tim.forward(100)
    
def tim_move_backwards():
    tim.backward(100)

def tim_move_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def tim_move_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
        
def tim_clear():
    tim.home()
    tim.clear()



t.listen()
t.onkey(tim_move_forwards, "w")
t.onkey(tim_move_backwards, "s")
t.onkey(tim_move_left, "a")
t.onkey(tim_move_right, "d")
t.onkey(tim_clear, "c")

    
       
my_screen.exitonclick()