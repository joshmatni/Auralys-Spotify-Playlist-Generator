from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import base64
import os
from flask import Flask, redirect, request, session, jsonify
import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyOAuth
import openai
from openai_integration import get_keywords_for_search

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888/callback/"
SCOPE = "playlist-modify-private playlist-modify-public"
app = Flask(__name__)

#! Redirect URI.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


@app.route('/create_playlist', methods=['POST'])
def generate_playlist():
    data = request.json
    user_prompt = data.get('prompt')
    user_id = sp.me()['id']
    
    # Interpret the prompt to determine search keywords (this function needs to be defined)
    search_keyword = get_keywords_for_search(user_prompt)
    
    # Search for tracks
    tracks = search_tracks(search_keyword)
    
    # Create playlist
    playlist_id = create_playlist(user_id, "Generated Playlist", tracks)
    
    if playlist_id:
        return jsonify({"status": "success", "playlist_id": playlist_id}), 200
    else:
        return jsonify({"status": "error", "message": "Could not create playlist"}), 500

def search_tracks(keyword):
    try:
        results = sp.search(q=keyword, limit=10, type='track')
        tracks = [track['id'] for track in results['tracks']['items']]
        return tracks
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def create_playlist(user_id, name, tracks):
    try:
        if not tracks:
            print("No tracks found with the given search criteria.")
            return None

        playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
        playlist_id = playlist['id']
        sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
        return playlist_id
    except Exception as e:
        print(f"An error occurred while creating the playlist: {e}")
        return None

"""def interpret_prompt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate search keywords for a Spotify playlist based on the following prompt: {prompt}\n\nSearch keywords:",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )

        search_keywords = response.choices[0].text.strip()
        return search_keywords

    except Exception as e:
        print(f"An error occurred while interpreting the prompt: {e}")
        return None
"""

if __name__ == '__main__':
    app.run(debug=True)




"""def search_tracks(sp, keywords):
    try:
        results = sp.search(q=keywords, limit=10, type='track')
        tracks = [track['id'] for track in results['tracks']['items']]
        return tracks
    except Exception as e:
        logging.error(f"Failed to search tracks: {str(e)}")
        return []

def create_playlist(sp, user_id, name, tracks):
    try:
        playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
        playlist_id = playlist['id']
        sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
        return playlist_id
    except Exception as e:
        logging.error(f"Failed to create playlist: {str(e)}")
        return None

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    data = request.json
    user_prompt = data.get('prompt')
    
    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))
    
    # Get the user's ID
    user_id = sp.me()['id']
    
    # Generate search keywords using OpenAI
    keywords = get_keywords_for_search(user_prompt)
    
    if keywords:
        # Search for tracks on Spotify
        tracks = search_tracks(sp, keywords)
        
        if tracks:
            # Create a new playlist with the found tracks
            playlist_id = create_playlist(sp, user_id, "Generated Playlist", tracks)
            
            if playlist_id:
                playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
                return jsonify({"status": "success", "playlist_url": playlist_url}), 200
            else:
                return handle_error("Failed to create playlist")
        else:
            return handle_error("No tracks found for the given keywords")
    else:
        return handle_error("Failed to generate search keywords")
        
        Make sure to update the REDIRECT_URI, CLIENT_ID, CLIENT_SECRET, and SCOPE variables with your own Spotify API credentials.
        
          """

#use the commented function if better than originals
