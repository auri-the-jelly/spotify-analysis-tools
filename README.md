# spotify-analysis-tools

Python scripts to generate json files for listening data.

pip install spotipy

Create an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) 
Copy the client ID and secret and add a redirect uri, something like https://localhost:8080

    export SPOTIPY_CLIENT_ID="client_id"
    export SPOTIPY_CLIENT_SECRET="client_secret"
    export SPOTIPY_REDIRECT_URI="redirect_URI"

You're all set! You can use any of the scripts in this repo now!

The code is in [api_tools](api_tools/). Run the scripts while in that directory.

data_tools is WIP

### [**god_help_me.py**](api_tools/god_help_me.py)
a terribly named script, but what it does is get every track you have ♥ed and save it in the [song_list.json](api_tools/json/song_list.json)

## Needs song_list.json

### [**analyze_artists.py**](api_tools/analyze_artists.py)
Compiles a list of artists you like and how many tracks you have by each of them. Creates [artist_list.json](api_tools/json/artist_list.json)

### [**analyze_decades.py**](api_tools/analyze_decades.py)
Compiles the release years of all your tracks and how many tracks each year contains. Creates decades_list.json

### [**analyze_features.py**](api_tools/analyze_features.py)
Takes a while to finish. It needs to make a lot of API calls.

Gets the [audio features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features) of each track and stores them in [track_features.json](api_tools/json/track_features.json) and collects the average in [average_feature.json](api_tools/json/average_feature.json). Some of them are borked because of Spotify though.

### [**analyze_genres.py**](api_tools/analyze_genres.py)
Same as above, takes time.

Gets the genres of each artist, stores the artist and genre in [artist_genre.json](api_tools/json/artist_genre.json), andd the number of tracks each genre contains in [genre_list.json](api_tools/json/genre_list.json).

### [**analyze_popularity.py**](api_tools/analyze_popularity.py)
Gets the popularity of each track and sorts them by popularity in [popularity_list.json](api_tools/json/popularity_list.json).

### [**analyze_time.py**](api_tools/analyze_time.py)
Gets the duration of each track and and how many songs there are of each duration. I have no idea why I wrote this, although, you may find it useful, idk.

### [**chart.py**](api_tools/chart.py)
Requires pandas and plotly

    pip install pandas
    pip install plotly

Charts a given json file. Provide file name and names for the axes and optionally threshold.

### [**collaborators.py**](api_tools/collaborators.py)
Find most frequent collaborators for a given artist. Creates or appends to [collaborators.json](api_tools/json/collaborators.json)

### [**find_artist_by_genre.py**](api_tools/find_artist_by_genre.py)
Find artist who make music in a given genre.

### [**find_by_feature.py**](api_tools/find_by_feature.py)
Find tracks which have a given feature above the specified threshold. Prefix a - for tracks below that threshold.

### [**find_songs_by_feature.py**](api_tools/find_songs_by_feature.py)
Make playlist of songs matching a feature threshold.

### [**populate_playlist.py**](api_tools/populate_playlist.py)
Requires a json file of tracks sorted by feature, created by [find_songs_by_feature.py](api_tools/find_songs_by_feature.py). Populates the playlist. 

### [**user_top.py**](api_tools/user_top.py)
Gets user's top tracks and collects them in [user_top_artists.json](api_tools/json/user_top_artists.json) and [user_top_tracks.json](api_tools/json/user_top_tracks.json).