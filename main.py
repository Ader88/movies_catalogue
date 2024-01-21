from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)

def tmdb_image_url(path, size="w342"):
    return tmdb_client.get_poster_url(path, size)

def get_movie_info(movie):
    return {
        "id": movie["id"],
        "title": movie["title"],
        "poster_url": tmdb_image_url(movie["poster_path"])
    }

def is_valid_list_type(list_type):
    # Sprawdź, czy wybrany typ listy istnieje w API
    available_list_types = ["popular", "top_rated", "upcoming", "now_playing"]
    return list_type in available_list_types

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')

    # Sprawdź, czy wybrany typ listy jest poprawny
    if not is_valid_list_type(selected_list):
        selected_list = 'popular'

    movies = tmdb_client.get_movies_list(list_type=selected_list)["results"]
    num_movies_to_display = 8
    movies_to_display = movies[:num_movies_to_display]
    movies_info = [get_movie_info(movie) for movie in movies_to_display]

    return render_template("homepage.html", movies=movies_info, tmdb_image_url=tmdb_image_url, current_list=selected_list)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast, tmdb_image_url=tmdb_image_url)

if __name__ == '__main__':
    app.run(debug=True)
