# TODO: Feature 3
from turtle import title
from flask.testing import FlaskClient
from src.repositories.movie_repository import _movie_repo
from src.models.movie import Movie


def test_search_movies_page(test_app: FlaskClient):
   # _movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    test_movie = test_app.post('/movies', data = {
        "mname": "Star Wars",
        "dname": "George Lucas", 
        "rating": 5, 
        }, follow_redirects=True
        )
    response_pass = test_app.get('/movies/search?title=Star%20Wars')
    response_fail = test_app.get('/movies/search?title=Justice+League')

    response_pass_data = response_pass.data
    response_fail_data = response_fail.data

    movie_in = _movie_repo.get_movie_by_title(response_pass_data)
    
    


    assert b'Star Wars' in response_pass_data
    assert b"Justice League" in response_fail_data


    