import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "user-library-read,playlist-modify-private,playlist-modify-public,user-library-modify"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
    )
)

playlist_id = "419QLuBISPzxfw8QyOQQoV"

playlist = sp.playlist(playlist_id)

artist_dict = {}

for track in playlist["tracks"]["items"]:
    for artist in track["track"]["artists"]:
        if artist["name"] in artist_dict.keys():
            artist_dict[artist["name"]] += 1
        else:
            artist_dict[artist["name"]] = 1

artist_dict = {
    k: v for k, v in sorted(artist_dict.items(), key=lambda item: item[1], reverse=True)
}

liked = open("json/artist_list.json")
liked_dict = json.load(liked)
liked.close()
total = 2718
percentage = {}
for artist, num in liked_dict.items():
    percentage[artist] = (num / total) * 100

with open("json/help.json", "w") as help_me_please:
    json.dump(artist_dict, help_me_please, indent=4)
with open("json/help2.json", "w") as help_me_please:
    json.dump(percentage, help_me_please, indent=4)
