from tkinter import *
from typing import Self
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"
WRONG_IMAGE_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/034_Day/QUIZ_FINAL_PROJECT/images/false.png"
TRUE_IMAGE_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/034_Day/QUIZ_FINAL_PROJECT/images/true.png"
FONT = ('Arial',20,'italic')
# Global Variables


# Implementation of User Interface of Quiz Screen
class UserInterface:

    def __init__(self, quiz_brain : QuizBrain):
      self.quiz = quiz_brain

      self.window = Tk()
      self.window.title("Quiz Game")
      self.window.config(pady=20, padx=20, background=THEME_COLOR)

      self.main_screen = Canvas(height=250, width=300, background="white")
      self.question_text = self.main_screen.create_text(125, 150, font=FONT, fill="black", text="Temporary Text",width=230)
      self.main_screen.grid(row=1, column=0, columnspan=2,padx=20,pady=20)
    
      self.wrong_image = PhotoImage(file=WRONG_IMAGE_FILE_PATH)
      self.wrong_button = Button(image=self.wrong_image, command=self.wrong_pressed,highlightthickness=0)
      self.wrong_button.grid(column=0, row=2, padx=20, pady=20)

      self.true_image = PhotoImage(file=TRUE_IMAGE_FILE_PATH)
      self.true_button = Button(image=self.true_image, command=self.true_pressed,highlightthickness=0)
      self.true_button.grid(column=1, row=2, padx=20, pady=20)
    
      self.score = 0
      self.score_label = Label(text=f"Score: {self.score}", foreground="white", background=THEME_COLOR)
      self.score_label.grid(column=1, row=0, padx=20, pady=20)
      


      self.next_question()
      self.window.mainloop()

    def next_question(self):
        self.main_screen.config(background="white")
        self.score_label.config(text=f"Score: {self.score}")
        if self.quiz.still_has_questions() == True:
            new_question = self.quiz.next_question()
            self.main_screen.itemconfig(self.question_text, text=new_question)
        else:
            self.main_screen.itemconfig(self.question_text, text="Game Over")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self) :
        self.give_feedback(self.quiz.check_answer("True"))
    
    def wrong_pressed(self) :
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right_or_wrong):
        if is_right_or_wrong == True:
            self.score +=1
            self.main_screen.config(bg="green") 
        else:
            self.main_screen.config(bg="red")
        self.window.after(1000, self.next_question)
    

