import os
import requests  
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
load_dotenv("/Users/lovely/Documents/Udemy/SECRET_API_KEYS/064_Day/.env")

# Constants
THE_MOVIES_DATABASE_API_KEY = os.getenv("TOP_10_MOVIES_API_KEY")
THE_MOVIES_DATABASE_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"




app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://///Users/lovely/Documents/Udemy/100_DaysOfProgramming/064_Day/day-64-starting-files-top-movies/movies.db"
Bootstrap5(app)

# Database Initalization
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app=app)


class Movie(db.Model):
    """This is the Components of a Movies Table by row"""
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    """This creates the desired Movies table listed above """
    db.create_all()

def top_10_list():
    """This Creates a Scalar Object in order of the ID primiary Key"""
    movies = db.session.execute(select(Movie).order_by(Movie.id)).scalars()
    return movies
    
# Class Functions
class EditForm(FlaskForm):
    """Creating Easy to use form uisng WTF Moudle"""
    edit_rating = DecimalField('ex: 10.0',places=2)
    edit_review = StringField()
    edit_submit = SubmitField('Done') 

class AddMovieTitle(FlaskForm):
    """Creating Easy to use form using WTF Module"""
    add_movie_title = StringField("Movie Title", validators=[DataRequired()])
    add_movie_title_submiti = SubmitField('Add Movie')


class TopMoviesDataBase(requests.Session):

    def __init__(self):
        super().__init__()

    def makeRequestAddCall(self, the_movies_database_parameter, url=THE_MOVIES_DATABASE_URL):
            response = self.get(url=url, params=the_movies_database_parameter)
            data = response.json()['results']
            return data
    
    def makeRequestFindCall(self, the_movies_database_parameter, url):
            response = self.get(url=url, params=the_movies_database_parameter)
            data = response.json()
            new_movie = Movie(
                 title= data["title"],
                 year= data["release_data"].split("-")[0],
                 img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
                 description= data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return new_movie
            
            
            
            




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

@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movies():
    form = AddMovieTitle()
    if form.validate_on_submit():
        top_movies_database = TopMoviesDataBase()
        movie_title = form.add_movie_title.data
        the_movies_database_parameter = {
        "api_key": THE_MOVIES_DATABASE_API_KEY,
        "query": movie_title
        }
        data = top_movies_database.makeRequestAddCall(the_movies_database_parameter=the_movies_database_parameter)
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)        

@app.route("/find")
def find_movie():
        movieTMDB = request.args.get("id")  
        if  movieTMDB:
            top_movies_database = TopMoviesDataBase()
            the_movies_database_parameter = {
            "api_key": THE_MOVIES_DATABASE_API_KEY,
            "language" : "en-US"
            }
            movieTMDB_url  = f"{THE_MOVIES_DATABASE_URL}/{movieTMDB}"
            movieTMDB_return = top_movies_database.makeRequestFindCall(url=movieTMDB_url,the_movies_database_parameter=the_movies_database_parameter)
            return redirect(url_for("edit", id=movieTMDB_return.id))
            




if __name__ == '__main__':
    app.run(debug=True)
