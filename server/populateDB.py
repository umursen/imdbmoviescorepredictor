import json
from re import sub

from imdb import IMDb

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from api.models import *

def readJSONFile():
    with open('../movies.json') as data_file:
        data = json.load(data_file)
        return data

def populateDjangoDB(data, movieLimit=500, castLimit=10):
    savedMovies=0

    for i in range(movieLimit):

        currentMovie = data[i]
        basicMovieInfo = ia.search_movie(currentMovie['name'])
        movieInfo = ia.get_movie(basicMovieInfo[0].movieID)

        if movieInfo['kind'].encode('utf-8').strip() == 'movie':

            movie, saved = Movie.objects.get_or_create(
            name=currentMovie['name'],
            release_date=currentMovie['release_date'],
            production_budget=sub(r'[^\d.]', '', currentMovie['production_budget']),
            domestic_gross=sub(r'[^\d.]', '', currentMovie['domestic_gross']),
            worldwide_gross=sub(r'[^\d.]', '', currentMovie['worldwide_gross']),
            )

            movie.writer = Person.objects.get_or_create(name = movieInfo['writer'][0]['name'].encode('utf8'))[0]
            movie.director = Person.objects.get_or_create(name = movieInfo['director'][0]['name'].encode('utf8'))[0]
            movie.year = movieInfo['year']

            if 'rating' in movieInfo.keys():
                movie.rating = movieInfo['rating']

            for n in range(castLimit):
                if n < len(movieInfo['cast']):
                    movie.casting.add(Person.objects.get_or_create(name=movieInfo['cast'][n]['name'].encode('utf8'))[0])

            for genre in movieInfo['genre']:
                movie.genre.add(Genre.objects.get_or_create(name=genre.encode('utf8'))[0])

            movie.save()

            savedMovies = savedMovies + 1

            print(str(i) + '-) Movie ' + movie.name + ' is saved!')
        else:
            print(str(i) + '-) Error: Couldnt find the movie. Instead, we have ' + currentMovie['name'].encode('utf-8').strip())

    print(str(savedMovies) + ' movies saved out of ' + str(i))



if __name__ == '__main__':
    ia = IMDb()
    data = readJSONFile()
    populateDjangoDB(data)
