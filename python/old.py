
def get_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'client_credentials'
    }
    # Encode client credentials for the request
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode())
    headers['Authorization'] = f"Basic {client_creds_b64.decode()}"

    response = requests.post(url, headers=headers, data=payload)
    token = response.json().get('access_token')
    return token

def get_track_info(access_token):
    url = 'https://api.spotify.com/v1/tracks/4cOdK2wGLETKBW3PvgPWqT'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    track_info = response.json()
    return track_info

# Usage
access_token = get_token()
track_info = get_track_info(access_token)
print(f"Access Token: {access_token}")
print("Track Info:", track_info)