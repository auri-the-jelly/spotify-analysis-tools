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

f = open("json/track_features.json", "r")
data = json.load(f)

feature = input("Feature: ").lower()
threshold = float(input("Threshold: "))

for track, feat_dict in data.items():
    if threshold > 0:
        if feat_dict[feature] > threshold:
            print(track)
    elif threshold < 0:
        if feat_dict[feature] < abs(threshold):
            print(track)
