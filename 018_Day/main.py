"""
import os 
from PIL import Image
import colorgram

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Image.jpg')
colors = colorgram.extract(image_path, 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


print(rgb_colors)
"""
import random
import turtle as tim
from turtle import Screen

tim.colormode(255)
t = tim.Turtle()
t.up()
t.hideturtle() 
t.speed("fastest")
my_screen = Screen()
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


t.setheading(225)
t.forward(400)
t.setheading(0)

for dot in range(1 , 130 + 1):
    t.dot(20 , (random.choice(color_list)))
    t.forward(60)

    if(dot % 10 == 0):
        t.setheading(90)
        t.forward(60)
        t.setheading(180)
        t.forward(600)
        t.setheading(0)

    


my_screen.exitonclick()