from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from openai_integration import get_keywords_for_search
import logging
import requests
from flask_cors import CORS

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "playlist-modify-private playlist-modify-public"

# Initialize Flask app and configure CORS
app = Flask(__name__)
CORS(app, origins=['http://localhost:3000/'])

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/api/openai', methods=['POST'])
def openai_api():
    data = request.json  # Retrieve JSON data from the request
    # Process the data, perform any necessary actions, and generate a response
    # For example, you can use `data` to call an external API or perform business logic
    
    # Create a response (e.g., a JSON response)
    response_data = {
        "text": "Processed data"  # Replace with actual response data
    }

    return jsonify(response_data), 200


@app.route('/create_playlist', methods=['POST'])
def generate_playlist():
    try:
        # Log incoming request data
        data = request.json
        print(data)
        logging.info(f"Incoming data: {data}")

        # Extract user prompt
        user_prompt = data.get('prompt')
        logging.info(f"user_prompt: {user_prompt}")

        # Get user ID
        user_id = sp.me()['id']
        logging.info(f"user_id: {user_id}")

        # Get search keyword
        search_keyword = get_keywords_for_search(user_prompt)
        logging.info(f"search_keyword: {search_keyword}")

        # Search for tracks
        if search_keyword:
            tracks = search_tracks(search_keyword)
            logging.info(f"Tracks found: {tracks}")

            # Create playlist if tracks found
            if tracks:
                playlist_id = create_playlist(user_id, "Generated Playlist", tracks)
                logging.info(f"playlist_id: {playlist_id}")

                # Return success response
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
        logging.info(f"Searching for keyword: {keyword}")
        # Search for tracks
        results = sp.search(q=keyword, limit=10, type='track')
        logging.info(f"Search results: {results}")

        # Extract track IDs
        tracks = [track['id'] for track in results['tracks']['items']]
        logging.info(f"Tracks found: {tracks}")
        return tracks
    except Exception as e:
        logging.error(f"An error occurred while searching tracks: {str(e)}")
        return []

def create_playlist(user_id, name, tracks):
    try:
        # Log playlist creation information
        logging.info(f"Creating playlist for user: {user_id} with name: {name}")
        logging.info(f"Tracks for playlist: {tracks}")

        # Check if tracks exist
        if not tracks:
            logging.warning("No tracks found with the given search criteria.")
            return None
        
        # Create a new playlist
        playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
        logging.info(f"Created playlist: {playlist}")

        # Get the playlist ID
        playlist_id = playlist['id']
        logging.info(f"Playlist ID: {playlist_id}")

        # Add tracks to the playlist
        sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
        logging.info(f"Added tracks to playlist: {tracks}")

        return playlist_id
    except Exception as e:
        logging.error(f"An error occurred while creating the playlist: {str(e)}")
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5000)
