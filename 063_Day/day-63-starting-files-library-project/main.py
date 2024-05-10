from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 
from sqlalchemy import Integer, String, Float

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
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/lovely/Documents/Udemy/100_DaysOfProgramming/063_Day/new-books-collection.db"


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app=app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<book {self.title}>'
    
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).order_by(Book.title).all()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        request_book = {
            "title" : request.form["title"],
            "author" : request.form["author"],
            "rating" : request.form["rating"]
        }
        with app.app_context():
            new_book = Book(title=request_book["title"], author=request_book["author"], rating=request_book["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect('/')
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    delete = db.get_or_404(Book, book_id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('home'))
    
if __name__ == "__main__":
    app.run(debug=True)

