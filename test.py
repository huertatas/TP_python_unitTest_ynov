import unittest
from unittest.mock import MagicMock
import requests
import json

class FilmsDB:
    def __init__(self):
        self.allFilms = None
        self.newFilm = None
        self.deletedFilmStatusCode = None
        self.updatedFilmResponse = None

    def getFilms(self):
        self.allFilms = requests.get("http://127.0.0.1:5000/getFilms").json()

    def postFilm(self, newFilm):
        self.newFilm = requests.get("http://127.0.0.1:5000/postFilm/" + str(newFilm)).json()['name']

    def deleteFilm(self, movieName):
        self.deletedFilmStatusCode = requests.get("http://127.0.0.1:5000/deleteFilm/" + str(movieName))
    
    def updateFilm(self, movieName, updatedName):
        self.updatedFilmResponse = requests.get("http://127.0.0.1:5000/updateFilm/" + str(movieName) + "/" +  str(updatedName)).json()['name']

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.filmTesting = FilmsDB()

    def tearDown(self):
        if self.filmTesting.newFilm:
            self.filmTesting.deleteFilm(self.filmTesting.newFilm)
        
    def test_getFilms(self):
        self.filmTesting.getFilms()
        self.assertIsNotNone(self.filmTesting.allFilms)

    def test_postFilm(self):
        self.filmTesting.postFilm("EssTestFilm")
        self.assertEqual("EssTestFilm", self.filmTesting.newFilm)
    
    def test_deleteFilm(self):
        newFilmToDelete = self.filmTesting.postFilm("EssTestFilm")
        self.filmTesting.deleteFilm(self.filmTesting.newFilm)
        self.assertEqual(self.filmTesting.deletedFilmStatusCode.status_code, 404)

    def test_updateFilm(self):
        newFilmToDelete = self.filmTesting.postFilm("UpdateTestFilm")
        self.filmTesting.updateFilm(self.filmTesting.newFilm, "NewNameTestFilm")
        self.filmTesting.newFilm = self.filmTesting.updatedFilmResponse
        self.assertEqual("NewNameTestFilm", self.filmTesting.updatedFilmResponse)

if __name__ == '__main__':
    unittest.main()        