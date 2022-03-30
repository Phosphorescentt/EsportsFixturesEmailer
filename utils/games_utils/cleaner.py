"""
A short script to take game data collected from the
https://api.pandascore.co/videogames endpoint and
remove the league information
"""

import json

with open("games") as g:
    data = json.load(g)

cleaned_data = []

for datum in data:
    d = {}
    d["id"] = datum["id"]
    d["name"] = datum["name"]
    d["slug"] = datum["slug"]

    cleaned_data.append(d)

with open("games2", "w") as f:
    json.dump(cleaned_data, f)

