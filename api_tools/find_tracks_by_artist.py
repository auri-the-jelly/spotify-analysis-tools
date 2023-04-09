import json
import time
import spotipy
import os
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

f = open("json/song_list.json", "r")
data = json.load(f)


search = input("Artist: ")

for song in data["items"]:
    artists = [artist["name"] for artist in song["track"]["artists"]]
    if search in artists:
        print(song["track"]["name"])
