import spotipy
import json
import random
import os
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read,playlist-modify-private,playlist-modify-public,user-library-modify"
playlust_id = "419QLuBISPzxfw8QyOQQoV"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
    )
)

song_dict = {}

songs = open("json/song_list.json", "r")
song_dict = json.load(songs)
songs.close()

numbers = []

for i in range(500):
    length = song_dict["total"]
    rangom = range(length)
    choice = random.choice(rangom)
    numbers.append(choice)

song_ids = []

for i in numbers:
    song_ids.append(song_dict["items"][i]["track"]["id"])

offset = [0, 100]

i = 500

while True:
    sp.playlist_add_items(playlust_id, song_ids[offset[0] : offset[1]])
    print("done ", offset[1])
    offset[0] += 100
    offset[1] += 100
    if offset[1] > i:
        if offset[1] != i + 100:
            offset[1] = i
        else:
            break
