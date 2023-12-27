from turtle import Turtle , Screen
from random import Random 
import os
random = Random()
race_on = False
my_screen = Screen()
my_screen.setup(width = 500 , height = 400)
user_bet = my_screen.textinput(title = "Make Your Bet" , prompt = "Which turtle will win the race?: Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
def initalize_game(): 
    global all_turtle
    for i in range(len(colors)):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        
        new_turtle.goto( x = -225, y = -100 + (i * 40))
        
        all_turtle.append(new_turtle)

initalize_game()

if user_bet: 
    race_on = True

while race_on:
        
    for turtle in all_turtle:
    
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've Won! {winning_color} turtle is the winner!")
            else: 
                print(f"You've Lost! {winning_color} turtle is the winner!")

        random_distance = random.randint(1,10)
        turtle.forward(random_distance)




my_screen.exitonclick()