from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    # Przykładowa lista filmów
    movies = [
        {"title": "Tytuł filmu 1", "image_url": "http://placehold.it/300x500"},
        {"title": "Tytuł filmu 2", "image_url": "http://placehold.it/300x500"},
        {"title": "Tytuł filmu 3", "image_url": "http://placehold.it/300x500"},
        {"title": "Tytuł filmu 4", "image_url": "http://placehold.it/300x500"}
    ]

    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
