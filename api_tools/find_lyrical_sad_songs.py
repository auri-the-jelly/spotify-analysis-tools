import json

with open("json/track_features.json", "r") as f:
    data = json.load(f)
    with open("json/sad_songs.json", "w") as sad_songs:
        i = 0
        sad_dict = {}
        for track, features in data.items():
            if (
                features["instrumentalness"] < 0.6
                and features["valence"] < 0.3
                and features["instrumentalness"] != 0
            ):
                sad_dict[track] = {
                    "instrumentalness": features["instrumentalness"],
                    "valence": features["valence"],
                }
        json.dump(sad_dict, sad_songs, indent=4)
