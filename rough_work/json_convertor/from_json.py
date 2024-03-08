#!/usr/bin/python3
"""Deserialization : convert and save json file to  dict data"""

import json

with open("data.json", "r") as json_file:
    infos = json.loads(json_file.read())
    # print(infos)
    # print()
    # print(infos[2])
    # print()
    # print(infos[2]["courses"][0])
    # Iterate over the list of dictionaries
    for info in infos:
        # Check if the value of the "id" key is equal to 2
        if info["id"] == 0:
            print(info)