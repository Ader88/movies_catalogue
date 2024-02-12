import unittest
from unittest.mock import Mock, patch
from tmdb_client import get_single_movie, get_poster_url, get_single_movie_cast

class TestTMDBClient(unittest.TestCase):

    @patch('tmdb_client.requests.get')
    def test_pobranie_danych_jednego_filmu(self, mock_get):
        # Przygotowanie zastępczej odpowiedzi
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 123, "title": "Testowy Film", "poster_path": "/test_poster_path"}
        mock_get.return_value = mock_response

        # Wywołanie funkcji
        movie_details = get_single_movie(123)

        # Aserty
        self.assertIsNotNone(movie_details)
        self.assertEqual(movie_details['id'], 123)
        self.assertEqual(movie_details['title'], "Testowy Film")
        self.assertEqual(movie_details['poster_url'], "https://image.tmdb.org/t/p/w342/test_poster_path")

    def test_pobranie_adresu_url_plakatu(self):
        # Test z poprawną ścieżką plakatu
        poster_url = get_poster_url("/test_poster_path")
        self.assertEqual(poster_url, "https://image.tmdb.org/t/p/w342/test_poster_path")

        # Test z pustą ścieżką plakatu
        poster_url = get_poster_url(None)
        self.assertIsNone(poster_url)

    @patch('tmdb_client.requests.get')
    def test_pobranie_listy_obsady_filmu(self, mock_get):
        # Przygotowanie zastępczej odpowiedzi
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"cast": [{"id": 1, "name": "Aktor 1"}, {"id": 2, "name": "Aktor 2"}]}
        mock_get.return_value = mock_response

        # Wywołanie funkcji
        movie_cast = get_single_movie_cast(123)

        # Aserty
        self.assertIsNotNone(movie_cast)
        self.assertEqual(len(movie_cast), 2)
        self.assertEqual(movie_cast[0]['id'], 1)
        self.assertEqual(movie_cast[0]['name'], "Aktor 1")
        self.assertEqual(movie_cast[1]['id'], 2)
        self.assertEqual(movie_cast[1]['name'], "Aktor 2")

if __name__ == '__main__':
    unittest.main()
