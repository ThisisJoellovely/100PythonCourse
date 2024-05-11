from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://///Users/lovely/Documents/Udemy/100_DaysOfProgramming/064_Day/day-64-starting-files-top-movies/movies.db"

Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app=app)

class Movie(db.Model):
    """This is the Components of a Movies Table by row"""
    id : Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False, unique=True)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    ranking : Mapped[int] = mapped_column(Integer, nullable=False)
    review : Mapped[str] = mapped_column(String, nullable=False)
    img_url : Mapped[str] = mapped_column(String, nullable=False, unique=True)

class EditForm(FlaskForm):
    """Creating Easy to use form uisng WTF Moudle"""
    edit_rating = DecimalField('ex: 10.0',places=2)
    edit_review = StringField()
    edit_submit = SubmitField('Done') 

with app.app_context():
    """This creates the desired Movies table listed above """
    db.create_all()

def top_10_list():
    movies = db.session.execute(select(Movie).order_by(Movie.id)).scalars()
    return movies
    


# with app.app_context(): 
#     first_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#     db.session.add(first_movie)
#     db.session.add(second_movie)
#     db.session.commit()
#     print("Process Completed")




@app.route("/")
def home():
    movies = top_10_list()
    return render_template("index.html", data=movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.edit_rating.data)
        movie.review = form.edit_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",data=movie,form=form)


if __name__ == '__main__':
    app.run(debug=True)
