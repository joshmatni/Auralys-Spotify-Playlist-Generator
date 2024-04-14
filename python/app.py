from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from openai_integration import get_keywords_for_search
import logging
import requests
from flask_cors import CORS


load_dotenv()
OPENAI_API_KEY="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"
CLIENT_ID="2cbb257b9e524eb18192f6ed664b0389"
CLIENT_SECRET="4082dbe7a2414177b91cd96f51845307"
REDIRECT_URI = "http://localhost:8888/callback/"
SCOPE = "playlist-modify-private playlist-modify-public"

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    #return render_template('index.html')
    return "Flask server is running!"

@app.route('/create_playlist', methods=['POST'])
def generate_playlist():
    try:
        data = request.json
        user_prompt = data.get('prompt')
        user_id = sp.me()['id']
        search_keyword = get_keywords_for_search(user_prompt)
        if search_keyword:
            tracks = search_tracks(search_keyword)
            if tracks:
                playlist_id = create_playlist(user_id, "Generated Playlist", tracks)
                if playlist_id:
                    return jsonify({"status": "success", "playlist_id": playlist_id}), 200
                else:
                    return jsonify({"status": "error", "message": "Could not create playlist"}), 500
            else:
                return jsonify({"status": "error", "message": "No tracks found"}), 404
        else:
            return jsonify({"status": "error", "message": "Could not extract search keywords"}), 400
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

def search_tracks(keyword):
    try:
        results = sp.search(q=keyword, limit=10, type='track')
        tracks = [track['id'] for track in results['tracks']['items']]
        return tracks
    except Exception as e:
        logging.error(f"An error occurred while searching tracks: {str(e)}")
        return []

def create_playlist(user_id, name, tracks):
    try:
        if not tracks:
            logging.warning("No tracks found with the given search criteria.")
            return None
        playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
        playlist_id = playlist['id']
        sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
        return playlist_id
    except Exception as e:
        logging.error(f"An error occurred while creating the playlist: {str(e)}")
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5000)




