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


load_dotenv("/Users/lovely/Documents/100_DaysOfProgramming/064_Day/064_Day:secretkey/.env")

# Constants
THE_MOVIES_DATABASE_API_KEY = os.getenv("TOP_10_MOVIES_API_KEY")
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
THE_MOVIES_DATABASE_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# ↓ CHANGED: was a hardcoded local path. Render can't access your machine.
#   Original: "sqlite://///Users/lovely/Documents/.../movies.db"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///movies.db")
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
                 year= data["release_date"].split("-")[0],
                 img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
                 description= data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return new_movie
            
    
@app.route("/")
def home():
    result = db.session.execute(select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
         all_movies[i].ranking = len(all_movies) - i
         db.session.commit()
         
    return render_template("index.html", data=all_movies)

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
        print(movieTMDB) 
        if  movieTMDB:
            top_movies_database = TopMoviesDataBase()
            the_movies_database_parameter = {
            "api_key": THE_MOVIES_DATABASE_API_KEY,
            "language" : "en-US"
            }
            movieTMDB_url  = f"{MOVIE_DB_INFO_URL}/{movieTMDB}"
            movieTMDB_movie = top_movies_database.makeRequestFindCall(url=movieTMDB_url,the_movies_database_parameter=the_movies_database_parameter)
            return redirect(url_for("edit", id=movieTMDB_movie.id))
        


if __name__ == '__main__':
    app.run(debug=True)
