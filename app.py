from flask import Flask, redirect, render_template

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies')
def list_all_movies():
    # TODO: Feature 1
    movieList = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movieList =movieList)


@app.route('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.route('/movies', methods=["POST"])
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
