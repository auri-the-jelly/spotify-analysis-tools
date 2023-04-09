import json
import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOT_ID = os.environ["SPOT_ID"]
SPOT_SEC = os.environ["SPOT_SEC"]

scope = "user-library-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOT_ID,
        client_secret=SPOT_SEC,
        redirect_uri="https://localhost:8080",
        scope=scope,
    )
)

if os.path.exists(os.path.join("json", "song_list.json")):
    f = open("json/song_list.json", "r")
else:
    f = open("api_tools/json/song_list.json", "r")
data = json.load(f)

album_ids = []
genres = {}
al_genres = {}
albums = {}
artists = {}

for song in data["items"]:
    for artist in song["track"]["artists"]:
        try:
            if artist["name"] not in artists.keys():
                print("getting")
                artist_spot = sp.artist(artist["id"])
                artists[artist["name"]] = artist_spot["genres"]
                print("new")
            else:
                artist_spot = {"genres": artists[artist["name"]]}
                print("pre-existing")
            print(artist["name"])
            for genre in artist_spot["genres"]:
                if genre in genres.keys():
                    genres[genre] += 1
                else:
                    genres[genre] = 1
        except:
            pass

genres = {
    k: v for k, v in sorted(genres.items(), key=lambda item: item[1], reverse=True)
}
al_genres = {
    k: v for k, v in sorted(al_genres.items(), key=lambda item: item[1], reverse=True)
}
for genre, num in genres.items():
    print(f"{genre}: {num}")
with open("json/a_genre_list.json", "w") as json_file:
    json.dump(genres, json_file, indent=4)
with open("json/artist_genre.json", "w") as artist_genre:
    json.dump(artists, artist_genre, indent=4)
