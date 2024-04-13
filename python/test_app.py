import pytest
from app import app, search_tracks, create_playlist
from unittest.mock import patch, MagicMock

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