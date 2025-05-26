from flask import Flask, render_template, request
from services import fetch_movie_data

app = Flask(__name__)

@app.route('/')
def home():
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

@app.route('/popular')
def popular():
    popular_titles = ["Inception", "The Dark Knight", "Titanic", "Interstellar", "The Matrix"]
    movies = [fetch_movie_data(title) for title in popular_titles if fetch_movie_data(title)]
    return render_template("popular.html", movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
