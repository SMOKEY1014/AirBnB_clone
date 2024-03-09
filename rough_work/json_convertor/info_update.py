#!/usr/bin/python3
"""this function checks and updates data with the given key"""

import json

def update(key, value):
    with open("data.json", "r") as json_file:
        infos = json.load(json_file)
        # Iterate over the list of dictionaries
        for info in infos:
            # Check if the value of the "id" key matches the provided id
            if (info["{key}"]):
                info["{key}"] = value
                return info
        # Return None if no matching id is found
        return None


id_to_find = 2
found_info = update(name, "ntuthuko" )
if found_info:
    print(found_info)
else:
    print(f"No info found with id {id_to_find}")