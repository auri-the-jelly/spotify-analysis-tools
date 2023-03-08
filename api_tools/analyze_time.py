import json
import time

f = open("json/song_list.json", "r")
data = json.load(f)

durations = {}

avg_dur = 0

i = 0

for song in data["items"]:
    duration = round((song["track"]["duration_ms"] / 1000) / 60, 1)
    if duration > 1.4:
        avg_dur += duration
        if not str(duration) in durations.keys():
            durations[str(duration)] = 1
        else:
            durations[str(duration)] += 1
        i += 1

avg_dur /= i
print(avg_dur)

durations = {
    k: v for k, v in sorted(durations.items(), key=lambda item: item[0], reverse=True)
}

with open("json/durations_list.json", "w") as json_file:
    json.dump(durations, json_file, indent=4)
