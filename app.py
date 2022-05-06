from flask import Flask, jsonify, request, redirect, make_response
from flask_pymongo import PyMongo
import requests


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://max:hh-123456789@cluster0.ba569.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo(app)

db_operations = mongo.db.films

@app.route('/testServer')
def testServer():
    return "App is working"

@app.route('/getFilms')
def getFilms():
    films = db_operations.find()
    allFilms = [{'film_name' : film['name']} for film in films]
    if allFilms:
        return jsonify(allFilms)
    else:
        return None


@app.route('/postFilm/<filmName>')
def postFilm(filmName):
    new_film = {'name' : filmName, 'image' : "no image", "video" : "no video", "category" : "test", "type:" : "test"}
    newFilmId = db_operations.insert_one(new_film)
    newFilm = db_operations.find_one({"name": filmName})
    if newFilm:
        return jsonify({"name": newFilm["name"]})
    else:
        return jsonify({"name": newFilm["error"]})

@app.route('/deleteFilm/<movieName>')
def deleteFilm(movieName):
    db_operations.delete_one({"name": movieName})
    filmDeleted = db_operations.find_one({"name": movieName})
    if filmDeleted: 
        return make_response("", 200)
    else:
        return make_response("", 404)

@app.route('/updateFilm/<filmName>/<newFilmName>')
def updateFilm(filmName, newFilmName):
    filmToUpdate = {"$set": {'name' : newFilmName}}
    filmToUpdateItem = {'name' : filmName}
    db_operations.update_one(filmToUpdateItem, filmToUpdate)
    newFilm = db_operations.find_one({"name": newFilmName})
    if newFilm:
        return jsonify({"name": newFilm["name"]})
    else:
        return jsonify({"name": newFilm["error"]})


if __name__ == '__main__':
    app.run(debug=True)