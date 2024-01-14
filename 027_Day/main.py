import tkinter

# Creating a main screen for all the object to reside in
main_screen = tkinter.Tk()
main_screen.geometry("215x80")
main_screen.title("Mile to Km Converter")


# Creating TKINTER objects for use in our main screen using a grid layout method
text_box = tkinter.Entry(width=10)
text_box.insert(tkinter.END, string="Welcome!")
text_box.grid(column=1, row=0)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0) 

is_equal_to_label = tkinter.Label(text="is equal to") 
is_equal_to_label.grid(column=0, row=2)

answer_label = tkinter.Label(text="0") 
answer_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row= 1) 

#Function for conversion between miles and Killometers
def conversion_method():
    user_input = text_box.get()
    float_kms = float(user_input) / 0.621371
    rounded_kms  = round(float_kms,2)
    string_rounded_kms = str(rounded_kms)
    answer_label.config(text=string_rounded_kms)

#GUI action implementation of the conversion function
calculate_button = tkinter.Button(text="Calulate",command=conversion_method)
calculate_button.grid(column=1, row=2)


main_screen.mainloop()

