import json

f = open("MyData/endsong_0.json")
f_2 = open("MyData/endsong_1.json")

json_1 = json.load(f)
json_1.extend(json.load(f_2))

f.close()
f_2.close()

device_dict = {}
seconds_played = 0
skipped_dict = {}

for track in json_1:
    platform = track["platform"].lower()
    if "linux" in platform:
        platform = "linux"
    elif "windows" in platform:
        platform = "windows"
    elif "android" in platform:
        platform = "android"
    if platform in device_dict.keys():
        device_dict[platform] += 1
    else:
        device_dict[platform] = 1

    seconds_played += track["ms_played"] / 1000

    if track["skipped"]:
        if track["master_metadata_track_name"] in skipped_dict.keys():
            skipped_dict[track["master_metadata_track_name"]] += 1
        else:
            skipped_dict[track["master_metadata_track_name"]] = 1

print(seconds_played / 3600)
device_dict = {
    k: v for k, v in sorted(device_dict.items(), key=lambda item: item[1], reverse=True)
}
skipped_dict = {
    k: v
    for k, v in sorted(skipped_dict.items(), key=lambda item: item[1], reverse=True)
}

with open("processed/devices.json", "w") as devices:
    json.dump(device_dict, devices, indent=4)
with open("processed/skipped.json", "w") as devices:
    json.dump(skipped_dict, devices, indent=4)

print(device_dict)
