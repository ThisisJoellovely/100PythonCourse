import random
from flask import Flask

guess_number = random.randint(0,9)
print(guess_number)

def CheckValidation(function):
    def wrapperFunction(*args):
        global guess_number
        if args[0] == guess_number:
            return '<h1 style="color:green;"><b>YOU FOUND ME!</b></h1></br> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh4MmthMDh0dGQzODdoMGZxYnowYWx3NDE4MHhiZXVmeXkxc2J2cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TdfyKrN7HGTIY/200.webp"></br>'
        elif args[0] < guess_number:
            return '<h1 style="color: red;"><b>Too low, Try again!</b></h1></br> <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm81ajN4ZGZtcXNkcGhldjdpbW9naWswbXp5N2FmaGx1ZmN1dWpoayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/EHRgFw83SaCB6EVALk/giphy.webp"></br>'
        else:
            return '<h1 style="color: red;"><b>Too High, Try again!</b></h1></br> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDY0ZG5sMDB6MGtwY200MTA4bTAxbW9lbmFtd2EyN21wNWhodjQzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l44QuS14nrX8SvGrC/giphy.gif"></br>'
    return wrapperFunction  


app = Flask(__name__)

@app.route('/')
def homePage(): 
    return '<h1><b>Guess A Number Between 0 - 9</b></h1></br> <img src= "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3c1MGgwcHNpNjQ0NGtwaHlxMjBiNDRxdWt0bWU5NzM1Z3hwZmkzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/89Eko49m84Ja/giphy.gif"></br>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > guess_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < guess_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True )