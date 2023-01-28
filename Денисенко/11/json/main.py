import json
import requests

GITHUB_API = 'https://api.github.com/users/'

response = requests.get(f'{GITHUB_API}rust-lang')

data = response.json()

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

