import requests

def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?apikey=6ebf4024&t={title}"
    response = requests.get(url).json()
    if response.get("Response") == "True":
        return response
    return None
