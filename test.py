import unittest
from unittest.mock import MagicMock
import requests
import json

class FilmsDB:
    def __init__(self):
        self.allFilms = None
        self.newFilm = None

    def getFilms(self):
        self.allFilms = requests.get("http://127.0.0.1:5000/getFilms").json()

    def postFilm(self, newFilm):
        self.newFilm = requests.get("http://127.0.0.1:5000/postFilm/" + str(newFilm)).json()


class TestFilm(unittest.TestCase):
    def setUp(self):
        self.filmTesting = FilmsDB()
        self.filmTesting.getFilms()
        self.filmTesting.postFilm("NewFilmTitle")
        
    def test_getFilms(self):
        self.assertIsNotNone(self.filmTesting.allFilms)

    def test_postFilm(self):
        self.assertEqual("NewFilmTitle", self.filmTesting.newFilm)

if __name__ == '__main__':
    unittest.main()        