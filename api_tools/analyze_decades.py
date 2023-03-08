import json
import time

f = open("json/song_list.json", "r")
data = json.load(f)

decades = {}

for song in data["items"]:
    release = song["track"]["album"]["release_date"]
    if "-" in release and release[0] != "2":
        release = release[: release.index("-") - 1] + "0"
    elif "-" in release and release[0] == "2":
        release = release[: release.index("-")]
    elif len(release) == 4:
        release = release[:3] + "0"
    if release in decades.keys():
        decades[release] += 1
    else:
        decades[release] = 1

decades = {
    k: v for k, v in sorted(decades.items(), key=lambda item: item[1], reverse=True)
}

with open("json/decades_list.json", "w") as json_file:
    json.dump(decades, json_file, indent=4)
