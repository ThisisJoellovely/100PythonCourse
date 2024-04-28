from flask import Flask, render_template
import requests
 
app = Flask(__name__)

data = []
try:
        with requests.get("https://api.npoint.io/c790b4d5cab58020d391") as connection:
            connection.raise_for_status()
            data = connection.json()
except requests.RequestException as e:
        print("Error:", e)

@app.route('/')
def home():
    return render_template("index.html",posts=data)

@app.route('/post/<int:num>')
def get_post(num):
      for item in data:
        if item["id"] == num:
            return render_template("post.html", post=item)
        
if __name__ == "__main__":
    app.run(debug=True)
