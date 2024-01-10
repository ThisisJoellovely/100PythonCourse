from turtle import Turtle
import os

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")
FILE_PATH = "File.txt"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ABS_FILE_PATH = os.path.join(SCRIPT_DIR, FILE_PATH)



class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open(ABS_FILE_PATH) as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(ABS_FILE_PATH,"w") as file:
                file.write(str(self.highscore))
        
            
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
