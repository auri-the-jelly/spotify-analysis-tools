import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read,user-top-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
    )
)

user_top_tracks = {}
user_top_artists = {}

user_top_tracks["short"] = [
    f"{track['artists'][0]['name']} - {track['name']}"
    for track in sp.current_user_top_tracks(limit=50, time_range="short_term")["items"]
]
user_top_tracks["medium"] = [
    f"{track['artists'][0]['name']} - {track['name']}"
    for track in sp.current_user_top_tracks(limit=50, time_range="medium_term")["items"]
]
user_top_tracks["long"] = [
    f"{track['artists'][0]['name']} - {track['name']}"
    for track in sp.current_user_top_tracks(limit=50, time_range="long_term")["items"]
]

user_top_artists["short"] = [
    f"{track['name']} - {track['popularity']}"
    for track in sp.current_user_top_artists(limit=50, time_range="short_term")["items"]
]
user_top_artists["medium"] = [
    f"{track['name']} - {track['popularity']}"
    for track in sp.current_user_top_artists(limit=50, time_range="medium_term")[
        "items"
    ]
]
user_top_artists["long"] = [
    f"{track['name']} - {track['popularity']}"
    for track in sp.current_user_top_artists(limit=50, time_range="long_term")["items"]
]

with open("json/user_top_tracks.json", "w") as top_json:
    json.dump(user_top_tracks, top_json, indent=4)
with open("json/user_top_artists.json", "w") as top_json:
    json.dump(user_top_artists, top_json, indent=4)
