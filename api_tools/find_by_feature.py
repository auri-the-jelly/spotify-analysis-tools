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

f = open("json/track_features.json", "r")
data = json.load(f)

feature = "valence"  # input("Feature: ").lower()
threshold = -0.3  # float(input("Threshold: "))

for track, feat_dict in data.items():
    if threshold > 0:
        if feat_dict[feature] > threshold:
            print(track)
    elif threshold < 0:
        if feat_dict[feature] < abs(threshold):
            print(track)
