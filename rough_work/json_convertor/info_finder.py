#!/usr/bin/python3
"""this function checks data with the given id"""

import json

def get_info_by_id(id):
    with open("data.json", "r") as json_file:
        infos = json.load(json_file)
        # Iterate over the list of dictionaries
        for info in infos:
            # Check if the value of the "id" key matches the provided id
            if info["id"] == id:
                return info
        # Return None if no matching id is found
        return None

# Example usage
id_to_find = 2
found_info = get_info_by_id(id_to_find)
if found_info:
    print(found_info)
else:
    print(f"No info found with id {id_to_find}")
