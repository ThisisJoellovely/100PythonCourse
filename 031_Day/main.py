# Import statements 
from tkinter import *
import pandas
import random
# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/031_Day/images/card_back.png" 
CARD_FRONT_FILE_PATH ="/Users/lovely/Documents/100_DaysOfProgramming/031_Day/images/card_front.png"
CARD_RIGHT_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/031_Day/images/right.png"
CARD_WRONG_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/031_Day/images/wrong.png"
FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/031_Day/data/words_to_learn.csv"
FILE_PATH_INITAL = "/Users/lovely/Documents/100_DaysOfProgramming/031_Day/data/french_words.csv"
TERM_FONT = ("Ariel",40,"italic" )
DEF_FONT = ("Ariel",60,"bold")

# Global Variables
data_dict = {}
current_card = {}
keys_list = []
flip_timer = None

# _____________________ Functions _______________________ 
def turn_file_into_dictonary():
    global data_dict
    global keys_list
    try:
        with open(FILE_PATH) as file:
            data = pandas.read_csv(file)
            keys_list = list(data.columns)
            data_dict = data.to_dict(orient="records")
    except FileNotFoundError:
        with open(FILE_PATH_INITAL) as file:
            data = pandas.read_csv(file)
            keys_list = list(data.columns)
            data_dict = data.to_dict(orient="records")
       
        
        
    
def flip_1():
    global data_dict
    global current_card
    global keys_list 
    global flip_timer
    
    flip_timer = main_screen.after_cancel(flip_timer)

    term = keys_list[0]
    current_card = random.choice(data_dict)
    card_canvas.itemconfig(card_term, text=term, fill="black")
    card_canvas.itemconfig(card_def, text=current_card[term], fill="black")
    card_canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = main_screen.after(3000,func=flip_2)

def flip_2():
    global keys_list
    global current_card
    
    definiton = keys_list[1]

    card_canvas.itemconfig(card_term, text=definiton, fill="white")
    card_canvas.itemconfig(card_def, text=current_card[definiton], fill="white")
    card_canvas.itemconfig(card_image, image=card_back_image)
    return 0

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv(FILE_PATH, index=False)
    flip_1()
    
# _____________________ UI IMPLEMENTATION _______________________
main_screen = Tk() 
main_screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
main_screen.title("Flash Card")
flip_timer = main_screen.after(3000,flip_2)

#Implementation of turning preloaded data file into a dictonary
turn_file_into_dictonary()

# Implementation for card center facing with both term and definition label
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR )
card_front_image = PhotoImage(file=CARD_FRONT_FILE_PATH)
card_back_image = PhotoImage(file=CARD_BACK_FILE_PATH)
card_image = card_canvas.create_image(400, 265, image=card_front_image)
card_def = card_canvas.create_text(400, 300, text="", font=DEF_FONT)
card_term = card_canvas.create_text(400, 200, text="", font=TERM_FONT)
card_canvas.grid(column=0,row=0,columnspan=2)

# Implementation of Right Button
right_image = PhotoImage(file=CARD_RIGHT_FILE_PATH)
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR,command=is_known)
right_button.grid(column=0, row=1)

# Implementation of Wrong Button 
wrong_image = PhotoImage(file=CARD_WRONG_FILE_PATH)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR,command=flip_1)
wrong_button.grid(column=1, row=1)









main_screen.mainloop()

