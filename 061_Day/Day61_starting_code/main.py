import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


load_dotenv('/Users/lovely/Documents/Udemy/SECRET_API_KEYS/061_Day/.env')

# CONSTANT VARIABLES
API_SECRET_KEY = os.environ['MY_SECREt_API_KEY']

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class LoginCredentials(FlaskForm):
        Email = StringField(label='Email', validators=[DataRequired(), Email()])
        Password = PasswordField(label='Password', validators=[DataRequired(), Length(1,8)])
        Submit = SubmitField(label='Log In')



app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = API_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET" , "POST"])
def login():
    login_form = LoginCredentials()
    if login_form.validate_on_submit():
         Email_data = login_form.Email.data 
         Password_data = login_form.Password.data
         if Email_data == "admin@email.com" and Password_data == "12345678":
            return render_template('success.html')
         else:
              return render_template('denied.html')
    
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

    
