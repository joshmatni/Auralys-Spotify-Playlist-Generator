
import pytest
from app import app, search_tracks, create_playlist
from unittest.mock import patch, MagicMock
import openai
"""
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_generate_playlist_success(client):
    mock_get_keywords_for_search = MagicMock(return_value="chill vibes")
    mock_search_tracks = MagicMock(return_value=["track1", "track2"])
    mock_create_playlist = MagicMock(return_value="playlist_id")

    with patch("app.get_keywords_for_search", mock_get_keywords_for_search), \
         patch("app.search_tracks", mock_search_tracks), \
         patch("app.create_playlist", mock_create_playlist):

        response = client.post("/create_playlist", json={"prompt": "chill music"})

        assert response.status_code == 200
        assert response.json == {"status": "success", "playlist_id": "playlist_id"}

def test_generate_playlist_no_tracks(client):
    mock_get_keywords_for_search = MagicMock(return_value="chill vibes")
    mock_search_tracks = MagicMock(return_value=[])
    mock_create_playlist = MagicMock(return_value=None)

    with patch("app.get_keywords_for_search", mock_get_keywords_for_search), \
         patch("app.search_tracks", mock_search_tracks), \
         patch("app.create_playlist", mock_create_playlist):

        response = client.post("/create_playlist", json={"prompt": "chill music"})

        assert response.status_code == 404
        assert response.json == {"status": "error", "message": "No tracks found"}

def test_generate_playlist_no_keywords(client):
    mock_get_keywords_for_search = MagicMock(return_value=None)

    with patch("app.get_keywords_for_search", mock_get_keywords_for_search):
        response = client.post("/create_playlist", json={"prompt": "chill music"})

        assert response.status_code == 400
        assert response.json == {"status": "error", "message": "Could not extract search keywords"}

def test_search_tracks():
    mock_sp = MagicMock()
    mock_sp.search.return_value = {"tracks": {"items": [{"id": "track1"}, {"id": "track2"}]}}

    with patch("app.sp", mock_sp):
        tracks = search_tracks("keyword")

        assert tracks == ["track1", "track2"]

def test_create_playlist_success():
    mock_sp = MagicMock()
    mock_sp.user_playlist_create.return_value = {"id": "playlist_id"}

    with patch("app.sp", mock_sp):
        playlist_id = create_playlist("user_id", "Playlist Name", ["track1", "track2"])

        assert playlist_id == "playlist_id"

def test_create_playlist_no_tracks():
    playlist_id = create_playlist("user_id", "Playlist Name", [])

    assert playlist_id is None
    """

def test_search_tracks_specific():
    # Define the expected response from the Spotify API
    expected_response = {
        "tracks": {
            "items": [
                {"id": "track1"},
                {"id": "track2"},
                {"id": "track3"}
            ]
        }
    }

    # Mock the Spotify client
    mock_sp = MagicMock()
    mock_sp.search.return_value = expected_response

    # Patch the Spotify client creation
    with patch("app.sp", mock_sp):
        # Call the function with specific keywords
        keywords = "upbeat workout music"
        tracks = search_tracks(keywords)

        # Assert the expected track IDs
        assert tracks == ["track1", "track2", "track3"]

        # Assert that the Spotify search method was called with the correct parameters
        mock_sp.search.assert_called_once_with(q=keywords, limit=10, type='track')   


# run this:    pytest test_app.py::test_search_tracks_specific




# Assuming 'app' is structured as Flask app instance and imported accordingly
"""from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_generate_playlist_specific(client):
    # Expected data setup
    expected_keywords = "keyword1, keyword2, keyword3"
    expected_playlist_id = "playlist123"

    # Mock the Spotify client
    mock_sp = MagicMock()
    mock_sp.me.return_value = {"id": "user123"}
    mock_sp.search.return_value = {"tracks": {"items": [{"id": "track1"}, {"id": "track2"}, {"id": "track3"}]}}
    mock_sp.user_playlist_create.return_value = {"id": expected_playlist_id}

    # Patch the OpenAI function and Spotify client
    with patch("app.sp", mock_sp), \
         patch("openai_integration.get_keywords_for_search", return_value=expected_keywords):

        # Send a POST request to the generate_playlist route with specific data
        data = {"prompt": "I want to listen to some upbeat music while working out"}
        response = client.post("/create_playlist", json=data)

        # Assertions
        assert response.status_code == 200
        assert response.json == {"status": "success", "playlist_id": expected_playlist_id}"""


from openai_integration import get_keywords_for_search

def test_get_keywords_for_search():
    # Define the prompt for the test
    prompt = "I want to listen to some upbeat music while working out"

    # Define the expected response from the OpenAI API
    expected_response = MagicMock()
    expected_response.choices = [MagicMock(text="keyword1, keyword2, keyword3")]

    # Mock the OpenAI API client
    mock_openai_client = MagicMock()
    mock_openai_client.chat.completions.create.return_value = expected_response

    # Patch the OpenAI client creation
    with patch("openai_integration.OpenAI", return_value=mock_openai_client):
        # Call the get_keywords_for_search function with the prompt
        keywords = get_keywords_for_search(prompt)

        # Assert the expected keywords
        assert keywords == ["keyword1", "keyword2", "keyword3"]

        # Assert that the OpenAI API was called with the correct parameters
        mock_openai_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in extracting keywords from the prompt for music searches."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=60
        )
        
    #run pytest test_openai_integration.py





    #   all tests, run seperate
    
    #   pytest test_app.py::test_search_tracks_specific
    #   pytest test_app.py::test_create_playlist_specific  
    #   pytest test_app.py::test_generate_playlist_specific
