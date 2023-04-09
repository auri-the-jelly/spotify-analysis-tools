import json
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord, "calplot")))
import pandas as pd
import calplot
import datetime
import seaborn as sns

f = open("MyData/endsong_0.json")
f_2 = open("MyData/endsong_1.json")

data = json.load(f)
data.extend(json.load(f_2))

f.close()
f_2.close()

import datetime

# create a dictionary to store the artist and track counts for each week
weekly_counts = {}

# iterate over the data and group the dictionaries by week
for d in data:
    # parse the timestamp string into a datetime object
    ts = datetime.datetime.strptime(d["ts"], "%Y-%m-%dT%H:%M:%SZ")
    # get the year and week number for the datetime object
    year, week, _ = ts.isocalendar()
    # create a key for the week in the weekly_counts dictionary
    week_key = (year, week)
    if week_key not in weekly_counts:
        weekly_counts[week_key] = {"artists": {}, "tracks": {}}
    # extract the artist and track names from the dictionary and increment the counts
    artist_name = d["master_metadata_album_artist_name"]
    track_name = d["master_metadata_track_name"]
    weekly_counts[week_key]["artists"][artist_name] = (
        weekly_counts[week_key]["artists"].get(artist_name, 0) + 1
    )
    weekly_counts[week_key]["tracks"][track_name] = (
        weekly_counts[week_key]["tracks"].get(track_name, 0) + 1
    )

# iterate over the weekly counts and select the favorite artist and track for each week
for week_key, counts in sorted(weekly_counts.items()):
    favorite_artist = max(counts["artists"], key=counts["artists"].get)
    favorite_track = max(counts["tracks"], key=counts["tracks"].get)
    print(
        f"Week {week_key}: Favorite Artist - {favorite_artist}, Favorite Track - {favorite_track}"
    )
