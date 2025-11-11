# api_investigation.py

import requests
import json


url = "https://api.acodingtutor.com/members/5?_delay=500"
response = requests.get(url)

data = response.json()

print (data)

print("Finished")