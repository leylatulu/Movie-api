import pandas as pd
from config import OMDB_API_KEY
import requests


MOVIE_NAME = ["the+office", "Twilight", "parasite", "The+Twilight+Saga%3A+New+Moon", "3+Idiots", "Up", "Ratatouille"]

def get_movie(response):
    all_data = []

    for item in response:
        data = {'Title': response['Title'],
                'Year': response['Year'],
                'Realeased':response['Released'],
                'Run Time': response['Runtime'],
                'Movie Type': response['Genre'],
                'Actors': response['Actors'],
                'Language': response['Language'],
                'Country': response['Country'],
                'Ratings': response['Ratings'][0]['Value'],
                'IMDB Rating': response['imdbRating'],
                'IMDB Votes': response['imdbVotes']
         
        }
    all_data.append(data)
    return pd.DataFrame(all_data)


def to_dataframe():
    all_url = []
    for movie in MOVIE_NAME:
        url_base = "http://www.omdbapi.com/?t=" + movie + "&plot=full&apikey=" + OMDB_API_KEY
        all_url.append(url_base)

    df = pd.DataFrame()
    for url in all_url:
        response = requests.get(url).json()
        df_movie = get_movie(response)
        df = pd.concat([df,df_movie])
    return df