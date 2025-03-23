import google.generativeai as genai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request, redirect, url_for

# Google Gemini API setup
API_KEY= "AIzaSyD9YyUfngDpj8kTBBQU-x-sQKEv-hfkd7c"
# Spotify API setup
genai.configure(api_key=API_KEY)
SPOTIFY_CLIENT_ID = "c3b5b5fe13ab44938d447811c65c97f9"
SPOTIFY_CLIENT_SECRET = "dec09afc691747c3affb34d548b42cc3"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

# Initialize Flask app
app = Flask(__name__)                                                          

# Function to get mood from text using Gemini API
def get_mood_from_text(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
    prompt = f"""
    Analyze the following user input and categorize the mood into one of the following:
    - Happy
    - Sad
    - Energetic
    - Relaxed
    - Angry
    - Romantic

    User input: "{user_input}"

    Respond only with the mood category.
    """
    response = model.generate_content(prompt)
    mood = response.text.strip()
    return mood

# Function to fetch playlist based on mood
def get_playlist_for_mood(mood):
    """Return a playlist ID based on the detected mood."""
    mood_playlists = {
        "Happy": "1llkez7kiZtBeOw5UjFlJq",  # Spotify's "Ultimate Happy Playlist"
        "Sad": "37i9dQZF1DX7qK8ma5wgG1",  # Spotify's "Sad Songs"
        "Energetic": "04sjCX94iFX3eENxph6eIN",  # Spotify's "Power Workout"
        "Relaxed": "37i9dQZF1DWU0ScTcjJBdj",  # Relaxing playlist
        "Angry": "37i9dQZF1EIgNZCaOGb0Mi",  # High-energy playlist
        "Romantic": "1YhWUX9r6jLnWBUTIwOo8C",  # Romantic songs playlist
    }

    # Return the playlist ID based on the detected mood
    return mood_playlists.get(mood, "3jfnlosjVZhBSZBqS2cJg7")  # Default to a general playlist

# Function to fetch and display tracks from the selected playlist
def get_playlist_tracks(playlist_id):
    playlist_tracks = sp.playlist_tracks(playlist_id)
    track_list = []

    for track in playlist_tracks['items']:
        track_list.append(f"{track['track']['name']} - {track['track']['artists'][0]['name']}")

    return track_list

def recommend_music_based_on_mood(user_text, genre=None, artist=None):
    """Recommend music based on detected mood and optional filters."""
    # Detect the mood from the user's text
    detected_mood = get_mood_from_text(user_text)
    print(f"Detected Mood: {detected_mood}")

    # Get the playlist ID based on the detected mood
    playlist_id = get_playlist_for_mood(detected_mood)

    # If a genre is specified, fetch a playlist based on the genre
    if genre:
        print(f"Fetching playlist for genre '{genre}'")
        playlist_id = get_playlist_for_genre(genre)

    # If an artist is specified, fetch tracks from that artist
    if artist:
        print(f"Fetching tracks by artist '{artist}'")
        tracks = get_tracks_by_artist(artist)
        return tracks  # Return tracks directly from the artist

    # Fetch and return tracks from the selected playlist
    tracks = get_playlist_tracks(playlist_id)
    return tracks
# user_text = "I feel like dancing....Hurray!."  # Example user input
# recommend_music_based_on_mood(user_text)

def get_playlist_for_genre(genre):
    """Fetch a playlist based on genre."""
    result = sp.search(q=f'genre:{genre}', type='playlist', limit=1)
    if result['playlists']['items']:
        return result['playlists']['items'][0]['id'] #'https://open.spotify.com/playlist/' +
    else:
        return None  # Return None if no playlist found

def get_tracks_by_artist(artists):
    tracks = []
    # Iterate through each artist and make individual search requests
    for artist_name in artists:
        result = sp.search(q=f'artist:{artist_name}', type='track', limit=10)

        # Collect the track names from the result
        for track in result['tracks']['items']:
            tracks.append(track['name'])

    return tracks
    # result = sp.search(q=f'artist:{artist}', type='track', limit=10)
    # tracks = []
    # for track in result['tracks']['items']:
    #     tracks.append(f"{track['name']} - {track['artists'][0]['name']}")
    # return tracks

# user_text = "Rihanna"  # Example user input
# get_tracks_by_artist(user_text.split(","))

# Main page (index)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['userText']
        genre = request.form['genre']
        artist = request.form['artist']

        detected_mood = get_mood_from_text(user_text)
        playlist_id = get_playlist_for_mood(detected_mood)

        # Fetch playlist based on mood
        tracks = recommend_music_based_on_mood(user_text, get_playlist_for_genre(genre), get_tracks_by_artist(artist.split(',')))

        return render_template('result.html', mood=detected_mood, tracks=tracks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
