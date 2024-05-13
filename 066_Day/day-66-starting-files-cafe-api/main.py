import random
from flask import Flask, jsonify, render_template, request
from sqlalchemy import func 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean , select
from flask_sqlalchemy import SQLAlchemy

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/lovely/Documents/Udemy/100_DaysOfProgramming/066_Day/day-66-starting-files-cafe-api/instance/cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}
    
   


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_GET_method():
    # FAILED ATTEMPT 
    #___
    # random_max = int(db.session.query(func.count(Cafe.id)).scalar())
    # random_number_domain = (0, (random_max))
    # random_number = random.randint(*random_number_domain)
    # get_cafe = db.session.query(Cafe).filter_by(id=random_number).first()
    # print(get_cafe.name)
    #__

    query = db.session.execute(select(Cafe))
    all_cafes = query.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe = random_cafe.to_dict())
    
@app.route("/all", methods=["GET"])
def all_GET_method():
    query = db.session.execute(select(Cafe))
    all_cafes = query.scalars().all()
    cafes_data = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=cafes_data)

@app.route("/search?<int:loc>", methods=["GET"])
def search_GET_method():

    
# HTTP POST - Create Record
@app.route("/random", methods=["POST"])
def random_POST_method():
    pass
# HTTP PUT/PATCH - Update Record
@app.route("/random", methods=["PUT", "PATCH"])
def radom_PUT_PATCH_method():
    pass
# HTTP DELETE - Delete Record
@app.route("/random", methods=["DELETE"])
def random_DELETE_method():
    pass

if __name__ == '__main__':
    app.run(debug=True)
