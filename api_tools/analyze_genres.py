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

f = open("json/song_list.json", "r")
data = json.load(f)

genres = {}
artists = {}

for song in data["items"]:
    for artist in song["track"]["artists"]:
        if not artist["name"] in artists.keys():
            artist_spot = sp.artist(artist["id"])
            artists[artist["name"]] = artist_spot["genres"]
            print(artist["name"])
            for genre in artist_spot["genres"]:
                if genre in genres.keys():
                    genres[genre] += 1
                else:
                    genres[genre] = 1

genres = {
    k: v for k, v in sorted(genres.items(), key=lambda item: item[1], reverse=True)
}
for genre, num in genres.items():
    print(f"{genre}: {num}")
with open("json/genre_list.json", "w") as json_file:
    json.dump(genres, json_file, indent=4)
with open("json/artist_genre.json", "w") as artist_genre:
    json.dump(artists, artist_genre, indent=4)
