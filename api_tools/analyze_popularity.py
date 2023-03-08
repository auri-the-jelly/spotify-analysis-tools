import json
import time

f = open("json/song_list.json", "r")
data = json.load(f)

popularities = {}

for song in data["items"]:
    name = song["track"]["artists"][0]["name"] + " - " + song["track"]["name"]
    popularity = song["track"]["popularity"]
    if name not in popularities.keys():
        popularities[name] = popularity
    elif popularity > popularities[name]:
        popularities["name"] = popularity

popularities = {
    k: v
    for k, v in sorted(popularities.items(), key=lambda item: item[1], reverse=True)
}

with open("json/popularity_list.json", "w") as json_file:
    json.dump(popularities, json_file, indent=4)
