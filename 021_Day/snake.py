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
        for position in STARTING_POSITIONS:   
           self.add_segment(position)
    
    def add_segment(self, position):
        new_segement = Turtle("square")
        new_segement.color("white")
        new_segement.speed("fastest")
        new_segement.penup() 
        new_segement.goto(position)
        self.snake.append(new_segement)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        
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
        