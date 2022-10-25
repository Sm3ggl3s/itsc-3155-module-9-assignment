# TODO: Feature 3

from src.repositories.movie_repository import _movie_repo

def test_get_movie_by_title():
    _movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    
    test_title = "Star Wars"
    test_title1 = "Thor"
    
    movie_title = _movie_repo.get_movie_by_title(test_title)

    assert movie_title.title != test_title1
    assert movie_title.title == test_title
    assert movie_title != ""