# TODO: Feature 1
from app import app, movie_repository
from src.repositories.movie_repository import get_movie_repository
import pytest
# TODO: Feature 1

@pytest.fixture(scope = 'module')
def testapp():
  return app.test_client()

def test_list_all_movies(testapp):
    movie_repository.create_movie('Batman', 'Bob', 5) 
    response = testapp.get('/movies')
    assert b'<th scope="col">Movie</th>' in response.data
    assert b'<th scope="row">Batman</th>' in response.data
    assert b'<td scope="row">5</td>' in response.data
    assert b'<td scope="row">Bob</td>'in response.data

    #wrong tests
    assert b'<th scope="row">bruh</th>' not in response.data
    assert b'<th scope="row">4</th>' not in response.data