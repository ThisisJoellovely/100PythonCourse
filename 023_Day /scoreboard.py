from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self,level):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = level
        self.update_scoreboard(level)

    def update_scoreboard(self,level):
        self.clear()
        self.level = level
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center",font=FONT)
