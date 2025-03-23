# # import google.generativeai as genai

# # # Replace with your actual API key
# # API_KEY = "AIzaSyD9YyUfngDpj8kTBBQU-x-sQKEv-hfkd7c"  # not to be shared publicly!
# # genai.configure(api_key=API_KEY)

# # def get_mood_from_text(user_input):
# #     """Analyze text input and extract a mood category."""
# #     model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"

# #     prompt = f"""
# #     Analyze the following user input and categorize the mood into one of the following:
# #     - Happy
# #     - Sad
# #     - Energetic
# #     - Relaxed
# #     - Angry
# #     - Romantic

# #     User input: "{user_input}"

# #     Respond only with the mood category.
# #     """

# #     response = model.generate_content(prompt)
# #     mood = response.text.strip()
# #     return mood

# # # Example usage
# # user_text = "I feel like dancing....Hurray!."
# # detected_mood = get_mood_from_text(user_text)
# # print(f"Detected Mood: {detected_mood}")

# # import spotipy
# # from spotipy.oauth2 import SpotifyClientCredentials

# # # Set up Spotify API
# # SPOTIFY_CLIENT_ID = "c3b5b5fe13ab44938d447811c65c97f9"
# # SPOTIFY_CLIENT_SECRET = "dec09afc691747c3affb34d548b42cc3"

# # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
# #                                                            client_secret=SPOTIFY_CLIENT_SECRET))

# # # Test: Get a playlist like...top playlist
# # playlist_id = "5ABHKGoOzxkaa28ttQV9sE"  # Spotify's "Top 100 most streamed"
# # playlist_tracks = sp.playlist_tracks(playlist_id)

# # # Print track names
# # for track in playlist_tracks['items']:
# #     print(track['track']['name'], "-", track['track']['artists'][0]['name'])

# import google.generativeai as genai
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# API_KEY = "AIzaSyD9YyUfngDpj8kTBBQU-x-sQKEv-hfkd7c" # Not to share it publicly!
# genai.configure(api_key=API_KEY)

# # Spotify Credentials
# SPOTIFY_CLIENT_ID = "c3b5b5fe13ab44938d447811c65c97f9"
# SPOTIFY_CLIENT_SECRET = "dec09afc691747c3affb34d548b42cc3"

# # Initialize Spotify client
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
#                                                            client_secret=SPOTIFY_CLIENT_SECRET))

# # Function to get mood from text using Gemini API
# def get_mood_from_text(user_input):
#     """Analyze text input and extract a mood category."""
#     model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"

#     prompt = f"""
#     Analyze the following user input and categorize the mood into one of the following:
#     - Happy
#     - Sad
#     - Energetic
#     - Relaxed
#     - Angry
#     - Romantic

#     User input: "{user_input}"

#     Respond only with the mood category.
#     """

#     response = model.generate_content(prompt)
#     mood = response.text.strip()
#     return mood

# # Function to fetch playlist based on mood
# def get_playlist_for_mood(mood):
#     """Return a playlist ID based on the detected mood."""
#     mood_playlists = {
#         "Happy": "1llkez7kiZtBeOw5UjFlJq",  # Spotify's "Ultimate Happy Playlist"
#         "Sad": "37i9dQZF1DX7qK8ma5wgG1",  # Spotify's "Sad Songs"
#         "Energetic": "04sjCX94iFX3eENxph6eIN",  # Spotify's "Power Workout"
#         "Relaxed": "37i9dQZF1DWU0ScTcjJBdj",  # Relaxing playlist
#         "Angry": "37i9dQZF1EIgNZCaOGb0Mi",  # High-energy playlist
#         "Romantic": "1YhWUX9r6jLnWBUTIwOo8C",  # Romantic songs playlist
#     }

#     # Return the playlist ID based on the detected mood
#     return mood_playlists.get(mood, "3jfnlosjVZhBSZBqS2cJg7")  # Default to a general playlist

# # Function to fetch and display tracks from the selected playlist
# def get_playlist_tracks(playlist_id):
#     """Fetch tracks from a specific Spotify playlist."""
#     playlist_tracks = sp.playlist_tracks(playlist_id)
#     track_list = []

#     # Collect track names and artists
#     for track in playlist_tracks['items']:
#         track_list.append(f"{track['track']['name']} - {track['track']['artists'][0]['name']}")

#     return track_list

# # Main flow: Mood detection and playlist fetching
# def recommend_music_based_on_mood(user_text):
#     """Recommend music based on detected mood."""
#     detected_mood = get_mood_from_text(user_text)
#     print(f"Detected Mood: {detected_mood}")

#     playlist_id = get_playlist_for_mood(detected_mood)
#     print(f"Fetching playlist for mood '{detected_mood}' (Playlist ID: {playlist_id})")

#     # Fetch and display tracks from the playlist
#     tracks = get_playlist_tracks(playlist_id)
#     print(f"\nRecommended Tracks for '{detected_mood}' mood:")
#     for track in tracks:
#         print(track)

# # Example usage
# user_text = "I feel like dancing....Hurray!."  # Example user input
# recommend_music_based_on_mood(user_text)

# """RECOMMENDATION"""

# def recommend_music_based_on_mood(user_text, genre=None, artist=None):
#     """Recommend music based on detected mood and optional filters."""
#     # Detect the mood from the user's text
#     detected_mood = get_mood_from_text(user_text)
#     print(f"Detected Mood: {detected_mood}")

#     # Get the playlist ID based on the detected mood
#     playlist_id = get_playlist_for_mood(detected_mood)

#     # If a genre is specified, fetch a playlist based on the genre
#     if genre:
#         print(f"Fetching playlist for genre '{genre}'")
#         playlist_id = get_playlist_for_genre(genre)

#     # If an artist is specified, fetch tracks from that artist
#     if artist:
#         print(f"Fetching tracks by artist '{artist}'")
#         tracks = get_tracks_by_artist(artist)
#         return tracks  # Return tracks directly from the artist

#     # Fetch and return tracks from the selected playlist
#     tracks = get_playlist_tracks(playlist_id)
#     return tracks
# user_text = "I feel like dancing....Hurray!."  # Example user input
# recommend_music_based_on_mood(user_text)

# def get_playlist_for_genre(genre):
#     """Fetch a playlist based on genre."""
#     result = sp.search(q=f'genre:{genre}', type='playlist', limit=1)
#     if result['playlists']['items']:
#         return 'https://open.spotify.com/playlist/' + result['playlists']['items'][0]['id']

#     else:
#         return None  # Return None if no playlist found

# def get_tracks_by_artist(artists):
#     tracks = []
#     # Iterate through each artist and make individual search requests
#     for artist_name in artists:
#         result = sp.search(q=f'artist:{artist_name}', type='track', limit=10)

#         # Collect the track names from the result
#         for track in result['tracks']['items']:
#             tracks.append(track['name'])

#     return tracks

# user_text = "Rihanna"  # Example user input
# get_tracks_by_artist(user_text.split(","))

