"""
A scrpt to make sure that cleaner.py has run correctly
"""

import json

from pprint import pprint

with open("games") as f:
    data =json.load(f)

pprint(data)
