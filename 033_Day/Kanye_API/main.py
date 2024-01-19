from tkinter import *
import requests

# Constants 
KANYE_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/033_Day/Kanye_API/kanye.png"
BACKGROUND_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/033_Day/Kanye_API/background.png"

def get_quote():
    connection = requests.get("https://api.kanye.rest")
    connection.raise_for_status()
    data = connection.json()
    canvas.itemconfig(quote_text,text=f"{data["quote"]}",fill="black")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_FILE_PATH)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Press for Kanye Quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_FILE_PATH)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()