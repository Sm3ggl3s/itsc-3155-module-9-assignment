# TODO: Feature 2
#from urllib import response
from app import app, movie_repository
import pytest

@pytest.fixture()
def test_app():
    return app.test_client()



def test_create_movies_e2e(test_app):
    response = test_app.get('/movies/new')
    response_data = response.data
    assert b'<h1 class="mb-5" id="center">Create Movie Rating</h1>' in response_data
    assert b'<input type="mname" name="mname"  class="form-control" id="mname" autocomplete="off">' in response_data
    assert b'<input name="dname" type="dname" class="form-control" id="dname" autocomplete="off">' in response_data
    assert b'<legend name="rating" id="rating" class="col-form-label col-sm-2 pt-0">Rating</legend>' in response_data
