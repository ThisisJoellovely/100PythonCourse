from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20 
UP = 90 
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    # Attributes
    

    # Default Constructor
    def __init__(self):
        "Creating Object of type 'Snake'"
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """Start up for the snake game"""
        for i in range(3):   
            new_T = Turtle("square")
            new_T.color("white")
            new_T.speed("fastest")
            new_T.penup() 
            new_T.goto(STARTING_POSITIONS[i])
            self.snake.append(new_T)
            
        
    def move_forward(self):
        """Specify where the first segment should move for the snake to follow that path"""
        for last_T in range(len(self.snake)-1,0,-1):
            one_less_than_last = self.snake[last_T - 1]
            one_less_than_last_xcor = one_less_than_last.xcor()
            one_less_than_last_ycor = one_less_than_last.ycor()
            self.snake[last_T].goto(one_less_than_last_xcor,one_less_than_last_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
       
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        