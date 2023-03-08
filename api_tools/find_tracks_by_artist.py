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


search = input("Artist: ")

for song in data["items"]:
    artists = [artist["name"] for artist in song["track"]["artists"]]
    if search in artists:
        print(song["track"]["name"])
