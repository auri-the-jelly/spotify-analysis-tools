import json
import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
    )
)

if os.path.exists(os.path.join("json", "collaborators.json")):
    print("exists")
    file = open("json/collaborators.json", "r")
    collaborators = json.load(file)
    file.close()
else:
    collaborators = {}

artist_id = "1vCWHaC5f2uS3yhpwWbIA6"

artist_name = sp.artist(artist_id)["name"]

if artist_name not in collaborators.keys():
    collaborators[artist_name] = {}

artist_albums = sp.artist_albums(artist_id=artist_id, limit=50)

if artist_albums["total"] > 50:
    offset = 50
    while len(artist_albums["items"]) < artist_albums["total"]:
        artist_albums["items"].extend(
            sp.artist_albums(artist_id=artist_id, limit=50, offset=offset)["items"]
        )
        offset += 50
        print(len(artist_albums["items"]))

for album in artist_albums["items"]:
    album_obj = sp.album(album_id=album["id"])
    if album_obj["album_type"] != "compilation":
        print(album["name"])
        for track in album_obj["tracks"]["items"]:
            for artist in track["artists"]:
                if artist["name"] != artist_name:
                    if artist["name"] in collaborators[artist_name].keys():
                        collaborators[artist_name][artist["name"]] += 1
                    else:
                        collaborators[artist_name][artist["name"]] = 1

file = open("json/collaborators.json", "w")
json.dump(collaborators, file, indent=4)
file.close()
