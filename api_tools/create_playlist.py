import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read,playlist-modify-private,playlist-modify-public,user-library-modify"
playlust_id = "3fb9C4dIK8ccKdq97onxhc"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="Client ID",
        client_secret="Client Secret",
        redirect_uri="https://localhost:8080",
        scope=scope,
    )
)

song_ids = []

with open("json/instrumentall_songs.json", "r") as f:
    data = json.load(f)
    genres = {
        k: v
        for k, v in sorted(data.items(), key=lambda item: item[1]["instrumentalness"])
    }
    i = 0
    with open("json/song_list.json", "r") as songs:
        song_dict = json.load(songs)
        for sad_song in genres.keys():
            for track in song_dict["items"]:
                if sad_song == track["track"]["name"]:
                    song_ids.append(track["track"]["id"])
                    i += 1
    """                
    with open("json/song_list.json", "r") as songs:
        song_dict = json.load(songs)
        for track in song_dict["items"]:
            if track["track"]["name"] in genres.keys():
                song_ids.append(track["track"]["id"])
                i += 1
                # sp.playlist_add_items(playlust_id, [track["track"]["id"]])"""

print(i)

offset = [0, 100]

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
