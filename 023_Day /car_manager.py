from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.random_cars = []
        self.head = 0
    
    def create_cars(self, number):
        """This method will create more cars after every level"""
        for i in range(number):
            # If head is less than this number than creating a car
            if (self.head > i):
                continue
            else:
                new_car = Turtle("square")
                new_car.shapesize(stretch_len=2,stretch_wid=1)
                new_color = random.randint(0,5)
                new_car.color(COLORS[new_color])
                new_car_randomx = random.randint(-280,280)
                new_car_randomy = random.randint(-250,250)
                new_car.penup()
                new_car.goto(new_car_randomx , new_car_randomy)
                self.random_cars.append(new_car)
                self.head += 1

    def moving_cars(self, level):
        """This method is moving all the cars at the same speed using the level we are currently on"""
        size_of_cars = len(self.random_cars)
        for i in range(size_of_cars):
            car = self.random_cars[i]
            car_currentycor = car.ycor()
            car_currentxcor = car.xcor()

            # Check if the car is at the end of the screen
            if (car_currentxcor <= -280):
                car.goto(280,car_currentycor)
            else:
                car_newxcor = car_currentxcor - STARTING_MOVE_DISTANCE - (level + MOVE_INCREMENT)  
                car.goto(car_newxcor,car_currentycor)

   





    
    

