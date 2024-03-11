#!/usr/bin/python3
from os.path import exists
import json
from os import path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User




class FileStorage:
    """
    Class for serializing and deserializing objects to and from a JSON file.
    """
    CLASS_LIST = {
        'Basemodel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'State': State,
        'Review': Review,
        'User': User
    }

    __file_path = "file.json"  # Path for the JSON file
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
        """Serializes the data to the JSON file."""
        serialised_objs = {}
        for key, obj in self.__objects.items():
            serialised_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialised_objs, file)

    def reload(self):
        """
        Attempts to deserialize the JSON file and load objects into the dictionary.

        If the file doesn't exist, it does nothing silently.
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialised_objs = json.load(file)
                for key, object_data in serialised_objs.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**object_data)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass