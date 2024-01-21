import requests

API_KEY = "89b4c87346aa6ee8bbdb70bb9631f099"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OWI0Yzg3MzQ2YWE2ZWU4YmJkYjcwYmI5NjMxZjA5OSIsInN1YiI6IjY1YWE3NWVmOGQ1MmM5MDEzMzgxZTFmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cSw7wnhpvM53bnbOIIj4TfUnlQGaBNADhwFBD8E7oo4"

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}" if poster_api_path else None

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "append_to_response": "credits"
    }
    response = requests.get(endpoint, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None

    if response.status_code == 200:
        movie_details = response.json()
        movie_details["poster_url"] = get_poster_url(movie_details.get("poster_path"))
        return movie_details
    else:
        print(f"Error: {response.status_code}")
        return None

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {
        "api_key": API_KEY
    }
    response = requests.get(endpoint, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None

    if response.status_code == 200:
        return response.json().get("cast", [])
    else:
        print(f"Error: {response.status_code}")
        return None

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None

    return response.json()
