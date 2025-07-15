import requests

url = "http://127.0.0.1:8000/generate"
data = {"prompt": "Hi"}

response = requests.post(url, json=data)
print(response.json())