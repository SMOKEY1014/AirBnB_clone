#!/usr/bin/python3
from os.path import exists
import json


class FileStorage:
    """
    Class for serializing and deserializing objects to and from a JSON file.
    """

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects keyed by "<class name>.id"

    def all(self):
        """
        Returns the dictionary containing all serialized objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the internal dictionary.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary to a JSON string and writes it to the file.
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Attempts to deserialize the JSON file and load objects into the dictionary.

        If the file doesn't exist, it does nothing silently.
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass