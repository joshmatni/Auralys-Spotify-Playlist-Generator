from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, redirect, request, jsonify, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler 
import logging
import requests
from flask_cors import CORS, cross_origin
import random


load_dotenv()
app = Flask(__name__)
#CORS(app) # origins=['http://localhost:3000']
CORS(app) # , resources={r"/*": {"origins": "*"}}, supports_credentials=True
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
openai_client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "playlist-modify-public playlist-modify-private"
cache_handler = FlaskSessionCacheHandler(session)

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, 
                        client_secret=CLIENT_SECRET, 
                        redirect_uri=REDIRECT_URI, 
                        scope=SCOPE, 
                        cache_handler=cache_handler,
                        show_dialog=True)

sp = spotipy.Spotify(auth_manager=sp_oauth)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home(): # the login for spotify
    # if not sp_oauth.validate_token(cache_handler.get_cached_token()):
    #     auth_url = sp_oauth.get_authorize_url()
    #     return redirect(auth_url)
    # return redirect(url_for('generate_playlist_route'))
    return "Flask server is running!"

@app.route('/callback')
def callback():
    try:
        code = request.args.get('code')
        token_info = sp_oauth.get_access_token(code)
        return redirect(url_for('generate_playlist_route'))
    except Exception as e:
        logging.error("Failed to retrieve token: {}".format(e))
        return jsonify({"error": str(e)}), 500


@app.route('/generate_playlist_route', methods=['POST'])
def generate_playlist_route():
    data = request.get_json()
    #print(f"DATAAAAA: {data}")
    #print(f"DATAAA PROMPT: {data['prompt']}")
    pre_keywords = data['prompt']
    if not data:
        return jsonify({"error": "Invalid request payload"}), 400
    keywords = get_keywords_for_search(pre_keywords, openai_client)
    playlist_id = generate_playlist(keywords)
    return jsonify({"playlist_id": playlist_id}), 200

@app.route('/get_playlists')
def get_playlists():
    # Add logic to retrieve and display playlists here
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    playlists = sp.current_user_playlists()
    playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
    playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])

    return playlists_html


def generate_playlist(keywords):
    try:
        user_id = sp.me()['id']
        tracks = []
        for keyword in keywords:
            tracks.extend(search_tracks(keyword))
        #print(f"TRACKS:{tracks}")
        if tracks:
            playlist_name = generate_playlist_name(keywords)
            playlist_id = create_playlist(user_id, playlist_name, tracks) # dynamic playlist name
            if playlist_id:
                return {"status": "success", "playlist_id": playlist_id, "playlist_url": f"https://open.spotify.com/playlist/{playlist_id}"}, 200
                #return {"status": "success", "playlist_id": playlist_id}, 200
            else:
                return {"status": "error", "message": "Could not create playlist"}, 500
        else:
            return {"status": "error", "message": "No tracks found"}, 404
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {"status": "error", "message": "Internal server error"}, 500


def search_tracks(keyword):
    #print(f"Searching for tracks with keyword: {keyword}")
    try:
        results = sp.search(q=keyword, limit=5, type='track')
        #print(f"Search results: {results}")
        return [track['id'] for track in results['tracks']['items']]
    except Exception as e:
        logging.error(f"Error searching for tracks: {str(e)}")
        return []

def create_playlist(user_id, name, tracks):
    if not tracks:
        logging.warning("No tracks found with the given search criteria.")
        return None
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
    sp.user_playlist_add_tracks(user_id, playlist_id=playlist['id'],tracks=tracks)
    #print("Tracks added to playlist:", tracks)
    return playlist['id']

def get_keywords_for_search(prompt: str, client: OpenAI):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
            "content": "You are an assistant skilled in extracting keywords from the prompt for playlist generation and music. If there are not enough keywords generate synonyms of the current keywords so that you output at least 15 keywords. Your response should only be a list of keywords, separated by commas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=60
    )
    keywords = response.choices[0].message.content
    keywords_list = keywords.split(", ")
    print(f"KEYWORD_LIST: {keywords_list}")
    return keywords_list
    #return list(keywords)
    logging.error(f"Failed to extract keywords: {str(e)}")

def generate_playlist_name(keywords):
    if len(keywords) >= 3:
        selected_keywords = random.sample(keywords, 3)  # Select three random keywords
        name = " - ".join(selected_keywords)
    else:
        name = " - ".join(keywords)  # If less than three, use all
    return f"AI Playlist - {name}"  # Prefix with a common theme phrase


if __name__ == '__main__':
    app.run(debug=True) # , host='0.0.0.0', port=5001
