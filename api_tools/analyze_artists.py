import json
import time

f = open("json/song_list.json", "r")
data = json.load(f)

artists = {}

for song in data["items"]:
    try:
        for artist in song["track"]["artists"]:
            if artist["name"] in artists.keys():
                artists[artist["name"]] += 1
            else:
                artists[artist["name"]] = 1
        print(song["track"]["name"])
    except TypeError:
        print(song)
        time.sleep(5)
    except KeyError:
        print(song.keys())
artists = {
    k: v for k, v in sorted(artists.items(), key=lambda item: item[1], reverse=True)
}
for artist, num in artists.items():
    print(f"{artist}: {num}")
with open("json/artist_list.json", "w") as json_file:
    json.dump(artists, json_file, indent=4)
