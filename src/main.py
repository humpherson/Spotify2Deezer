import os
import requests
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_PLAYLIST_ID = os.getenv("SPOTIFY_PLAYLIST_ID")
DEEZER_USER_ID = os.getenv("DEEZER_USER_ID")

# Step 1: Get Spotify Access Token
def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET,
    }
    response = requests.post(auth_url, data=auth_data)
    response_data = response.json()
    return response_data.get("access_token")

# Step 2: Create a Deezer Playlist
def create_deezer_playlist(name="New Playlist"):
    url = f"https://api.deezer.com/user/{DEEZER_USER_ID}/playlists"
    response = requests.post(url, data={'title': name})
    
    if response.status_code == 200:
        playlist_id = response.json().get("id")
        print(f"Deezer playlist '{name}' created with ID: {playlist_id}")
        return playlist_id
    else:
        print("Failed to create Deezer playlist:", response.status_code)
        return None

# Step 3: Add Tracks to Deezer Playlist
def add_tracks_to_deezer_playlist(playlist_id, track_ids):
    url = f"https://api.deezer.com/playlist/{playlist_id}/tracks"
    response = requests.post(url, data={'songs': ','.join(track_ids)})
    
    if response.status_code == 200:
        print("Tracks added successfully to Deezer playlist.")
    else:
        print("Failed to add tracks to Deezer playlist:", response.status_code)

# Step 4: Retrieve Tracks from Spotify and Search on Deezer
def get_playlist_tracks(token):
    playlist_url = f"https://api.spotify.com/v1/playlists/{SPOTIFY_PLAYLIST_ID}/tracks"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(playlist_url, headers=headers)
    
    if response.status_code == 200:
        tracks = response.json().get("items", [])
        deezer_track_ids = []
        
        for item in tracks:
            track = item["track"]
            track_name = track["name"]
            artists = ", ".join(artist["name"] for artist in track["artists"])
            
            # Search for Track on Deezer
            deezer_track = search_deezer_track(track_name, artists)
            if deezer_track:
                deezer_track_ids.append(str(deezer_track["id"]))
        
        # Create a Deezer playlist and add tracks if any were found
        if deezer_track_ids:
            playlist_id = create_deezer_playlist("My Transferred Playlist")
            if playlist_id:
                add_tracks_to_deezer_playlist(playlist_id, deezer_track_ids)
    else:
        print("Failed to retrieve playlist tracks:", response.status_code)

# Step 5: Search Deezer for Track
def search_deezer_track(track_name, artists):
    search_query = f"{track_name} {artists}"
    url = f"https://api.deezer.com/search?q={search_query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json().get("data", [])
        if results:
            return results[0]  # Return the first matching track
    return None

if __name__ == "__main__":
    token = get_spotify_token()
    if token:
        get_playlist_tracks(token)
