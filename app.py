from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
API_KEY = '6ebf4024'

@app.route('/')
def home():
    return '''
        <form action="/movie" method="get">
            <input name="title" placeholder="Enter movie title">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/movie')
def movie():
    title = request.args.get('title')
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url).json()
    
    if response.get('Response') == 'False':
        return f"<h2>Movie not found: {title}</h2>"

    return render_template_string("""
        <h1>{{ movie['Title'] }}</h1>
        <p><strong>Year:</strong> {{ movie['Year'] }}</p>
        <p><strong>Plot:</strong> {{ movie['Plot'] }}</p>
        <img src="{{ movie['Poster'] }}" width="200">
        <br><a href="/">Search another</a>
    """, movie=response)

if __name__ == '__main__':
    app.run(debug=True)
