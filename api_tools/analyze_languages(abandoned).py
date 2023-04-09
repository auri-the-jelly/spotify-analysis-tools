import lyricsgenius
import os
import musixmatch
from langdetect import detect_langs

apikey = os.environ['MUSIXMATCH_KEY']
token = os.environ["GENIUS_TOKEN"]
genius = lyricsgenius.Genius(token)
f = open("json/song_list.json", "r")
json_data = json.load(f)
with open("json/langs.json", "w") as lang_file:
    lang_dict = {"tracks" : {}, "num": {}}
    for item in json_data['items']:
        track = item['track']
        artist = track["artists"][0]
        g_artist = genius.search_artist(artist["name"])
        g_track = g_artist.song(track['name'])
        m_track = musixmatch.track.search(q_track=track["name"],q_artist=artist["name"])
        if g_track:
            lyrics = g_track.lyrics
        else:
            lyrics = ""
        lang_dict[f"{artist['name']} - {track['name']}"] = detect_langs(lyrics)
