import json
import datetime

with open("json/top_500_list.json") as json_file:
    data = json.load(json_file)

    years = {
        "years": {},
        "longest": {"name": "", "time": 0},
        "shortest": {"name": "", "time": 100000000000000},
        "decades": {},
        "average": 0,
    }

    for song in data["items"]:
        release = song["track"]["album"]["release_date"]
        added = song["added_at"]
        if "-" in release:
            release = release.split("-")
            added = added[: added.index("T")].split("-")
            if len(release) == 3:
                release_epoch = int(
                    datetime.datetime(
                        int(release[0]), int(release[1]), int(release[2])
                    ).strftime("%s")
                )
                added_epoch = int(
                    datetime.datetime(
                        int(added[0]), int(added[1]), int(added[2])
                    ).strftime("%s")
                )
                if int(release[0]) > 2011:
                    diff = (added_epoch - release_epoch) / 86400
                    if diff > years["longest"]["time"]:
                        years["longest"]["name"] = song["track"]["name"]
                        years["longest"]["time"] = diff
                    if diff < years["shortest"]["time"]:
                        years["shortest"]["name"] = song["track"]["name"]
                        years["shortest"]["time"] = diff
        if type(release) == list:
            if release[0] in years["years"].keys():
                years["years"][release[0]] += 1
            else:
                years["years"][release[0]] = 1
            decade = release[0][:3] + "0s"
            if decade in years["decades"].keys():
                years["decades"][decade] += 1
            else:
                years["decades"][decade] = 1
        else:
            if release in years["years"].keys():
                years["years"][release] += 1
            else:
                years["years"][release] = 1
            decade = release[:3] + "0s"
            if decade in years["decades"].keys():
                years["decades"][decade] += 1
            else:
                years["decades"][decade] = 1

    years["years"] = {
        k: v
        for k, v in sorted(
            years["years"].items(), key=lambda item: item[1], reverse=True
        )
    }
    years["decades"] = {
        k: v
        for k, v in sorted(
            years["decades"].items(), key=lambda item: item[1], reverse=True
        )
    }

    with open("json/top_years_list.json", "w") as json_file:
        json.dump(years, json_file, indent=4)
