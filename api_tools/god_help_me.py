import spotipy
import json
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
song_dict = {}
song_dict = sp.current_user_saved_tracks(limit=50, offset=0)
offset = 50
while True:
    song_dict["items"].extend(
        sp.current_user_saved_tracks(limit=50, offset=offset)["items"]
    )
    print("done " + str(offset))
    offset += 50
    if offset > song_dict["total"]:
        if offset != song_dict["total"] + 50:
            offset = song_dict["total"]
        else:
            break

pop_list = [
    "available_markets",
    "disc_number",
    "explicit",
    "external_ids",
    "external_urls",
    "href",
    "is_local",
    "track_number",
]
album_pop = [
    "album_type",
    "artists",
    "available_markets",
    "external_urls",
    "href",
    "images",
    "name",
    "release_date_precision",
    "total_tracks",
]

for song in song_dict["items"]:
    for popper in pop_list:
        song["track"].pop(popper)
    for popper in album_pop:
        song["track"]["album"].pop(popper)

with open("json/song_list.json", "w") as json_file:
    json.dump(song_dict, json_file, indent=4)
