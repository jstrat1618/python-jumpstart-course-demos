import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")


search = 'capital'
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)

movie_data = resp.json()

movie_list = movie_data.get('hits')

movies = []
#Splice out the data from the movie into a named tuple
#for md in movie_list:
#    movie = MovieResult(
#        imdb_code=md.get('imdb_code'),
#        title=md.get('title'),
#        duration=md.get('duration'),
#        director=md.get('director'),
#        year=md.get('year', 0),
#        rating=md.get('rating', 0),
#        imdb_score=md.get('imdb_score', 0.0),
#        keywords=md.get('keywords'),
#        genres=md.get('genres')
#    )
#    movies.append(movie)

#A more efficient way is to use kwargs
#for md in movie_list:
#   movie = MovieResult(**md)
#    movies.append(movie)

#Even more efficiently we can use List comprehension with **kwargs
movies = [MovieResult(**md) for md in movie_list]

print("Found {} movies".format(len(movies)))
for m in movies:
    print("{}--{}".format(m.title, m.year))