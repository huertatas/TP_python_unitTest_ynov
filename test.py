import unittest
from unittest.mock import MagicMock
import requests
import json

class FilmsDB:
    def __init__(self):
        self.allFilms = None
        self.newFilm = None
        self.deletedFilm = None

    def getFilms(self):
        self.allFilms = requests.get("http://127.0.0.1:5000/getFilms").json()

    def postFilm(self, newFilm):
        self.newFilm = requests.get("http://127.0.0.1:5000/postFilm/" + str(newFilm)).json()

    def deleteFilm(self, id):
        self.deletedFilm = requests.get("http://127.0.0.1:5000/deleteFilm/" + str(id)).json()["message"]


## liste d'id pour tester le "delete"



class TestFilm(unittest.TestCase):
    def setUp(self):
        self.filmTesting = FilmsDB()
        
    def test_getFilms(self):
        self.filmTesting.getFilms()
        self.assertIsNotNone(self.filmTesting.allFilms)

    def test_postFilm(self):
        self.filmTesting.postFilm("NewFilmTitle")
        self.assertEqual("NewFilmTitle", self.filmTesting.newFilm)
    
    def test_deleteFilm(self):
        response = self.filmTesting.deleteFilm("621a14ee20a454cddc750ae2s")
        self.assertEqual(response.satus_code, 404)

if __name__ == '__main__':
    unittest.main()        