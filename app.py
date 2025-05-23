from flask import Flask, render_template, request
from services import fetch_movie_data

app = Flask(__name__)

@app.route('/')
def home():
    # الصفحة الرئيسية تعرض نموذج البحث فقط
    return render_template("home.html")

@app.route('/movie')
def movie():
    title = request.args.get('title')
    if not title:
        return render_template("home.html")
    
    movie = fetch_movie_data(title)
    return render_template("search.html", movie=movie)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

