from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#CONSTANTS
IMAGE_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/029_Day/logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(): 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for item in range(nr_letters)]
    password_list += [random.choice(symbols) for item in range(nr_symbols)]
    password_list += [random.choice(numbers) for item in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_textbox.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_string = website_textbox.get()
    username_string = username_textbox.get()
    password_string = password_textbox.get()
    new_data = { 
        website_string: {
        "email": username_string,
        "password": password_string,
    }}
    if len(website_string) == 0 or len(password_string) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the boxes empty")
    else:
        try:
            with open("data.json", "r") as file:
                #Reading JSON data file 
                data = json.load(file)
                #Updating with new data from what we have created
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            json.update(new_data)
            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:  
            website_textbox.delete(0,END)
            username_textbox.delete(0,END)
            password_textbox.delete(0,END)
            return 0
# ---------------------------- UI SETUP ------------------------------- #

# Implemenration of the screen class
main_screen = Tk()
main_screen.title("Password Manager") 
main_screen.config(padx=50, pady=50)

# Implementation of the canvas which will hold a image used for the main picture
main_canvas = Canvas(width=200, height=200)
password_manager_image = PhotoImage(file=IMAGE_FILE_PATH)
main_canvas.create_image(100, 100, image=password_manager_image)
main_canvas.grid(row=0, column=1)

# Implementation of 'website' label 
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Implemetation of 'Email/Username' label
Username_label = Label(text="Email/Username:")
Username_label.grid(column=0, row=2)

# Implementation of 'password' label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Implementation of website_textbox 
website_textbox = Entry(width=38)
website_textbox.focus()
website_textbox.grid(column=1, columnspan=2, row=1)

# Implementation of username_textbox 
username_textbox = Entry(width=38)
username_textbox.insert(0, "Joellovely0717@gmail.com")
username_textbox.grid(column=1, columnspan=2, row=2)

# Implementation of password_textbox 
password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3)

# Implementation of 'generate password' button
generate_password_button = Button(text="Generate Pasword", command=password_generator)
generate_password_button.grid(column=2, row=3)

# Implementation of 'add' button
add_button = Button(text="add", width= 36, command=save)
add_button.grid(column=1, columnspan=2,  row=4)

main_screen.mainloop() 