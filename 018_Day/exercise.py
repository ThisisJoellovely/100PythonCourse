import turtle as t
from turtle import Screen
import random  
# First challenege is to draw a square
tim = t.Turtle()
t.colormode(255)
my_screen = Screen()
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
"""
tim.forward(50)
tim.right(90)
tim.forward(50)
tim.right(90)
tim.forward(50)
tim.right(90)
tim.forward(50)
"""

"""
# Second Challenege is to create a dashed line with 50 dashes
tim.left(90)
for _ in range(15):
    tim.forward(5)
    tim.up()
    tim.forward(5)
    tim.down()
tim.backward(150)
"""

"""
# Third Challenege is to create a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon in different colors
tim.home()
tim_sides = [3, 4, 5, 6, 7, 8, 9, 10]
tim_colors = ['RoyalBlue', 'LightGray', 'SteelBlue', 'DarkSlateGray', 'LimeGreen', 'Olive', 'DarkGoldenrod', 'Orange']

for i in range(len(tim_sides)):
    tim.color(tim_colors[i])

    for j in range(tim_sides[i]):
        tim.forward(100)
        tim.right(360 / tim_sides[i])
"""

"""
# Fourth Challenge is to create a random walk
tim.home()

tim_directions = [0 ,90 ,180 ,270]
tim.width(3)
tim.speed("fastest")

for _ in range(250):
    tim.color(random_color())
    
    tim.forward(30)
    tim.setheading(random.choice(tim_directions))
"""

"""
# Fifth Challenge making a spirograph

def draw_siprograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):        
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_siprograph(5)
"""


my_screen.exitonclick()
