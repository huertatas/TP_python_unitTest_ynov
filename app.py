from flask import Flask, jsonify, request, redirect
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
    output = [{'film_name' : film['name']} for film in films]
    return jsonify(output)


@app.route('/postFilm/<filmName>')
def postFilm(filmName):
    new_film = {'name' : filmName, 'image' : "no image", "video" : "no video", "category" : "test", "type:" : "test"}
    newFilmId = db_operations.insert_one(new_film).inserted_id
    newFilm = db_operations.find_one({"_id": newFilmId})
    return jsonify(new_film["name"])

@app.route('/deleteFilm/<filmName>')
def deleteFilm(filmName):
    filmToDelete = {'name' : filmName}
    db_operations.delete_one(filmToDelete)
    result = {'result' : 'Deleted successfully'}
    return result

@app.route('/updateFilm/<filmName>/<newFilmName>')
def updateFilm(filmName, newFilmName):
    filmToUpdate = {"$set": {'name' : newFilmName}}
    filmToUpdateItem = {'name' : filmName}
    db_operations.update_one(filmToUpdateItem, filmToUpdate)
    result = {'result' : 'Updated successfully'}
    return result


if __name__ == '__main__':
    app.run(debug=True)