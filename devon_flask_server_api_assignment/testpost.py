import requests
import json

# Define the URL of your Flask server
url = 'http://127.0.0.1:8080/process'

# Dictionary with the data you want to send in JSON format
data = {
    "prompt": "Your prompt text here",
    "user": "Username"
}

# Send the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful:")
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)