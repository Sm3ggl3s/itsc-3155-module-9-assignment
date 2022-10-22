from app import app
from src.repositories.movie_repository import get_movie_repository
# TODO: Feature 1

movie_repository = get_movie_repository()

def test_list_all_movies():
    test_app = app.test_client()
    response = test_app.get('/movies')
  #  movie_repository.create_movie(self, Batman, Bob, 5) #
    assert b'Movie' in response.data