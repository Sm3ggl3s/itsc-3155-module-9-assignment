# TODO: Feature 2
from app import app, movie_repository
import pytest


@pytest.fixture()
def test_app():
    return app.test_client()


def test_create_movies(test_app):
    response = test_app.post("/movies", data={
        "mname": "HI",
        "dname": "Steve",
        "rating": "3"
    })

    movieEx = movie_repository.create_movie("HI", "Steve", "3")
    assert movieEx in movie_repository.get_all_movies()

    # Test for false positive
    assert not movie_repository.get_movie_by_title("Jurassic")

