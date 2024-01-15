from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/028_Day/Final_Project/tomato.png"
CHECK_MARK = "✓"
# ---------------------------- GLOBAL ------------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps

    reps = 0 
    main_screen.after_cancel(timer)
    tomato_canvas.itemconfig(tomato_timer_text, text="00:00")
    timer_text.config(text="-TIMER-")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mech():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # logic sytax of application 
    if(reps % 2 == 1 and reps != 8):
        timer_text.config(text="Work:", font=((FONT_NAME),50,"bold"), fg=GREEN, bg=YELLOW)
        count_down(work_sec)
    elif (reps % 2 == 0 and reps == 8):
        timer_text.config(text="Break:", font=((FONT_NAME),50,"bold"), fg=PINK, bg=YELLOW)
        count_down(long_break_sec) 
        reps = 0
    elif (reps % 2 == 0 and reps != 8):
        timer_text.config(text="Break:", font=((FONT_NAME),50,"bold"), fg=RED, bg=YELLOW)
        count_down(short_break_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    tomato_canvas.itemconfig(tomato_timer_text, text=f"{count_min}:{count_sec}") 
    if count > 0:
       timer = main_screen.after(1000, count_down, count - 1)
    else:
        timer_mech()
        check_string = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_string += CHECK_MARK
        check_label.config(text=check_string)
   
# ---------------------------- UI SETUP ------------------------------- #
# Implementation of main screen 
main_screen = Tk()
main_screen.title("Pomodoro Timer")
main_screen.config(padx=100, pady=50, bg=YELLOW)

# Implementation of Tomato with upper-layer Tomato Image
tomato_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=TOMATO_FILE_PATH)
tomato_canvas.create_image(100, 114, image=tomato_image)
tomato_timer_text = tomato_canvas.create_text(100,  130, text="00:00", fill="white", font= ((FONT_NAME),35,"bold"))
tomato_canvas.grid(row=1, column=1)

# Implementation of Timer Text
timer_text = Label(text="-TIMER-")
timer_text.config(font=((FONT_NAME),50,"bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(row=0, column=1)

# Implementation of Start Button 
start_button = Button(text="Start: ->", command=timer_mech)
start_button.config(font=((FONT_NAME),10,"bold"), fg=GREEN, bd=0)
start_button.grid(row=2, column=0)


# Implementation of Reset button
reset_button = Button(text="Reset: -x")
reset_button.config(font=((FONT_NAME),10,"bold"), fg=GREEN, bd=0, command=timer_reset)
reset_button.grid(row=2, column=2)
# Implementation of Check mark

check_label = Label()
check_label.config(font=((FONT_NAME),40,"bold"), fg=GREEN, bg=YELLOW,bd=0)
check_label.grid(row=4, column=1)



main_screen.mainloop()