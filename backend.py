import json as json
import requests as requests

with open("./secret.json") as f:
  api_key = json.load(f)["api-key"]

r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': 'Make sure you understand multiple perspectives, because',
    },
    headers={'api-key': api_key}
)

print(r.json()["output"])
