import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import os

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
genre_dict = {}
artist_dict = {}
analyses_dict = {"time_signature": {}, "key": {}, "tempo": 0}
features_dict = {
    "danceability": 0,
    "energy": 0,
    "valence": 0,
    "acousticness": 0,
    "instrumentalness": 0,
    "speechiness": 0,
}

playlist_url = "https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza"
# "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=95b071f453eb4196"


song_dict = sp.playlist_items(playlist_url)

total = song_dict["total"]

keys_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

offset = 100

while offset < total:
    song_dict["items"].extend(sp.playlist_items(playlist_url, offset=offset)["items"])
    offset += 100

print("songs added")

ids = []
artist_ids = []

for song in song_dict["items"]:
    ids.append(song["track"]["id"])
    for artist in song["track"]["artists"]:
        if artist["name"] in artist_dict.keys():
            artist_dict[artist["name"]] += 1
        else:
            artist_dict[artist["name"]] = 1
        artist_ids.append(artist["id"])


artists = sp.artists(artist_ids[:25])
offset = 0
while True:
    offset += 25
    if offset > total:
        break
    artists["artists"].extend(sp.artists(artist_ids[offset : offset + 25])["artists"])
for artist in artists["artists"]:
    for genre in artist["genres"]:
        if genre not in genre_dict.keys():
            genre_dict[genre] = 1
        else:
            genre_dict[genre] += 1

print("artists and genre added")

features = sp.audio_features(ids[:25])
offset = 0
while True:
    offset += 25
    if offset > total:
        break
    features.extend(sp.audio_features(ids[offset : offset + 25]))

i = 0
for feature_track in features:
    if feature_track:
        for feature, value in feature_track.items():
            if feature in features_dict.keys():
                features_dict[feature] += value
        i += 1

print("features added")

offset = 0
while True:
    if offset > total - 1:
        break
    analyses = sp.audio_analysis(ids[offset])
    analyses_dict["tempo"] += analyses["track"]["tempo"]
    time_signature = analyses["track"]["time_signature"]
    if time_signature in analyses_dict["time_signature"].keys():
        analyses_dict["time_signature"][time_signature] += 1
    else:
        analyses_dict["time_signature"][time_signature] = 1
    key = keys_list[analyses["track"]["key"]]
    mode = " major" if analyses["track"]["mode"] == 1 else " minor"
    key = str(key) + mode
    if key in analyses_dict["key"].keys():
        analyses_dict["key"][key] += 1
    else:
        analyses_dict["key"][key] = 1
    offset += 1

analyses_dict["tempo"] /= total

print(i)

print("analyses added")

genre_dict = {
    k: v for k, v in sorted(genre_dict.items(), key=lambda item: item[1], reverse=True)
}

artist_dict = {
    k: v for k, v in sorted(artist_dict.items(), key=lambda item: item[1], reverse=True)
}

for key, value in features_dict.items():
    features_dict[key] = round(value / total, 3)

with open("json/top_list.json", "w") as json_file:
    json.dump(song_dict, json_file, indent=4)

with open("json/top_genres_list.json", "w") as json_file:
    json.dump(genre_dict, json_file, indent=4)

with open("json/top_features_list.json", "w") as json_file:
    json.dump(features_dict, json_file, indent=4)

with open("json/top_artists_list.json", "w") as json_file:
    json.dump(artist_dict, json_file, indent=4)

with open("json/top_analysis_list.json", "w") as json_file:
    json.dump(analyses_dict, json_file, indent=4)
