from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        tempString = "<em><b>" + function() + "</b></em>"
        return tempString
    return wrapper

@app.route('/')
@make_bold
def helloworld():
    return "Hello, World!"

@app.route('/bye')
def bye():
    return "bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"hey {name} your {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)