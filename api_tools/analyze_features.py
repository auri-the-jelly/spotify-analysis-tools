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

f = open("json/song_list.json", "r")
json_data = json.load(f)
total = len(json_data["items"])
data = json_data["items"]

song_dict = sp.current_user_saved_tracks(limit=1, offset=0)
ids = []

feature_list = {
    "acousticness": 0,
    "danceability": 0,
    "energy": 0,
    "instrumentalness": 0,
    "liveness": 0,
    "loudness": 0,
    "speechiness": 0,
    "tempo": 0,
    "valence": 0,
}

track_features = {}

print(sp.audio_features([data[2692]["track"]["id"]]))

pop_list = [
    "key",
    "mode",
    "type",
    "id",
    "uri",
    "track_href",
    "analysis_url",
    "duration_ms",
    "time_signature",
]

i = 0
limit = [0, 100]
while i < total:
    if limit[1] > len(data):
        limit[1] = len(data)
    for j in range(limit[0], limit[1]):
        ids.append(data[j]["track"]["id"])
        i += 1
    features = sp.audio_features(ids)
    for feature in features:
        for pop in pop_list:
            feature.pop(pop)
    ids = []
    print("done ", i)
    track_index = limit[0]
    for j in range(50):
        track_features[data[track_index]["track"]["name"]] = features[j]
        for audio_feature in feature_list.keys():
            feature_list[audio_feature] += features[j][audio_feature]
        track_index += 1

    limit[0] += 100
    limit[1] += 100

for feature in feature_list:
    feature_list[feature] = round(feature_list[feature] / total, 3)

print(feature_list)

with open("json/track_features.json", "w") as json_file:
    json.dump(track_features, json_file, indent=4)

with open("json/average_feature.json", "w") as json_file:
    json.dump(feature_list, json_file, indent=4)
