import json
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="Client ID",
        client_secret="Client Secret",
        redirect_uri="https://localhost:8080",
        scope=scope,
    )
)

f = open("json/artist_genre.json", "r")
data = json.load(f)

genres = {}
artists = []

genre = input("Genre: ")

for artist, genre_list in data.items():
    if len(genre.split()) > 1:
        if genre in genre_list:
            print(artist)
