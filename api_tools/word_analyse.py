import json

songs_f = open("json/song_list.json", "r")
songs = json.load(songs_f)
top_songs_f = open("json/top_500_list.json")
top_songs = json.load(top_songs_f)

words_dict = {}
top_words_dict = {}

banlist = [
    "ft.",
    "(ft." "feat.",
    "(feat.",
    "(with",
    "remix",
    "remastered",
    "radio",
    "edit",
    "mix",
    "avicii",
    "version",
    "original",
    "extended",
    "acoustic",
    "instrumental",
    "remaster",
    "2011",
    "justin",
    "bieber",
    "bieber)",
    "lil",
    "cardi",
    "drake",
    "drake)",
]

for song in songs["items"]:
    name = song["track"]["name"]
    split_name = name.split()
    for word in split_name:
        combo = (
            word + " " + split_name[split_name.index(word) + 1]
            if split_name.index(word) + 1 < len(split_name)
            else ""
        )
        word = word.lower()
        if word not in banlist and len(word) > 2:
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1
            if combo and combo.split(" ")[1].lower() not in banlist:
                combo = combo.lower()
                if combo in words_dict.keys():
                    words_dict[combo] += 1
                else:
                    words_dict[combo] = 1


for song in top_songs["items"]:
    name = song["track"]["name"]
    split_name = name.split()
    for word in name.split(" "):
        combo = (
            word + " " + split_name[split_name.index(word) + 1]
            if split_name.index(word) + 1 < len(split_name)
            else ""
        )
        word = word.lower()
        if word not in banlist and len(word) > 2:
            if word in top_words_dict.keys():
                top_words_dict[word] += 1
            else:
                top_words_dict[word] = 1
            if combo and combo.split(" ")[1].lower() not in banlist:
                combo = combo.lower()
                if combo in top_words_dict.keys():
                    top_words_dict[combo] += 1
                else:
                    top_words_dict[combo] = 1

words_dict = {
    k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
}

top_words_dict = {
    k: v
    for k, v in sorted(top_words_dict.items(), key=lambda item: item[1], reverse=True)
}

with open("json/top_words_list.json", "w") as json_file:
    json.dump(top_words_dict, json_file, indent=4)

with open("json/words_list.json", "w") as json_file:
    json.dump(words_dict, json_file, indent=4)

songs_f.close()
top_songs_f.close()
