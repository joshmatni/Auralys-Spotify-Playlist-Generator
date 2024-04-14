import requests

# URL of your Flask application
url = 'http://127.0.0.1:5000//create_playlist'

# Example user prompt
user_prompt = "I want a playlist with the latest hip hop hits"

# Prepare the JSON data to send
data = {
    'prompt': user_prompt
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(response.status_code)
print(response.json())
