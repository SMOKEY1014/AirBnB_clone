#!/usr/bin/python3
"""Serialization : convert and save dict data to json file"""
import json

# Create a list of dictionaries
infos = [
    {
        "id" : 0,
        "name" : "John",
        "courses" : ["Maths", "English", "Science"]
    },
    {
        "id" : 1,
        "name" : "Jane",
        "courses" : ["History", "Geography", "Art"]
    },
    {
        "id" : 2,
        "name" : "Alice",
        "courses" : ["Physics", "Chemistry", "Biology"]
    }
]

# Converting data to json format
json_string = json.dumps(infos)
print(json_string)

# Saving json format to a file
with open("data.json", "a") as json_file:
    json.dump(infos, json_file, indent=2)
