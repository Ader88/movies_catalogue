from unittest.mock import Mock
from main import app
import pytest
import requests
import tmdb_client
import os

API_TOKEN = os.getenv("TMDB_API_TOKEN")

@pytest.fixture
def mock_get_movies_list(monkeypatch):
    mock_response = {'results': []}
    monkeypatch.setattr("requests.get", Mock(return_value=Mock(json=Mock(return_value=mock_response))))

def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.get_movies_list", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type='popular')

@pytest.mark.parametrize("list_type", ["popular", "top_rated", "upcoming", "now_playing"])
def test_homepage_with_list_type(monkeypatch, list_type, mock_get_movies_list):
    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        requests.get.assert_called_once_with(f"https://api.themoviedb.org/3/movie/{list_type}", headers={"Authorization": f"Bearer {API_TOKEN}"})
