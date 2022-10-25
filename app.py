from flask import Flask, redirect, render_template, request


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

    title = request.form.get('mname')
    director = request.form.get('dname')
    rating = request.form.get('rating')
    movie_repository.create_movie(title,director,rating)
    return redirect('/movies')


@app.route('/movies/search', methods = ["GET"])
def search_movies():
    # TODO: Feature 3
    search_title = request.args.get('title', type = str)
    
    movie_title = movie_repository.get_movie_by_title(search_title)
    
    print(search_title)
    return render_template('search_movies.html', search_active=True, movie = movie_title)
