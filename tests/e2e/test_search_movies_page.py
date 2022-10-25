# TODO: Feature 3
from turtle import title
from flask.testing import FlaskClient
from src.repositories.movie_repository import _movie_repo
from src.models.movie import Movie


def test_search_movies_page(test_app: FlaskClient):
    _movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    test_movie = test_app.post('/movies', data = {
        "title": 
    })
    response_pass = test_app.get('/movies/search?title=Star+Wars')
    response_fail = test_app.get('/movies/search', data ={
    "title ": "Justice League"})

    response_pass_data = response_pass.data
    response_fail_data = response_fail.data

    


    assert b"Star Wars" in response_pass_data


    