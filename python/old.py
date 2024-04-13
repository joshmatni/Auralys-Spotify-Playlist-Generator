#Old app.py

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



if __name__ == '__main__':
    app.run(debug=True)
