import requests

def fetch_movie_data(title):
    try:
        cleaned_title = title.strip()
        url = f"http://www.omdbapi.com/?apikey=6ebf4024&t={cleaned_title}"
        headers = {
            "User-Agent": "MovieInfoApp/1.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            print(f"Error: {data.get('Error')}")
    except requests.RequestException as e:
        print(f"Network error: {e}")
    return None
