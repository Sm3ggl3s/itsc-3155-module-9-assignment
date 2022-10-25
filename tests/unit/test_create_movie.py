# TODO: Feature 2
from app import app, movie_repository
import pytest
from src.models.movie import Movie


@pytest.fixture()
def test_app():
    return app.test_client()


def test_create_movies(test_app):
    response = test_app.post("/movies", data={
        "mname": "Hi",
        "dname": "Steve",
        "rating": 3
    })

    state = False
    movieEx = Movie("Hi", "Steve", 3)
    movieEx.__dict__
    for i in movie_repository.get_all_movies():
        if movieEx.__dict__ == i.__dict__:
            state = True

    # assert movieEx in movie_repository.get_all_movies()
    assert state
    # Test for false positive


def test_fp_create_movie(test_app):
    response = test_app.post("/movies", data={
        "mname": "Hi",
        "dname": "Steve",
        "rating": 3
    })

