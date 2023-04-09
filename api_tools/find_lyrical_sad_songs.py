import json

with open("json/track_features.json", "r") as f:
    data = json.load(f)
    with open("json/happy_songs.json", "w") as sad_songs:
        i = 0
        sad_dict = {}
        for track, features in data.items():
            if features["danceability"] > 0.69:
                sad_dict[track] = {
                    "danceability": features["danceability"],
                }
        json.dump(sad_dict, sad_songs, indent=4)
