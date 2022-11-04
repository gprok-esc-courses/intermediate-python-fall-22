import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

data = json.loads(response.text)

print(data['value'])
