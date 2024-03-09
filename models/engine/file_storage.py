#!/usr/bin/python3
from models.base_model import BaseModel
from os.path import exists
import json

class FileStorage:
    """This class  serializes instances to a JSON file and deserializes JSON file to instances"""
    CLASSES = {
        'BaseModel': BaseModel
    }
    __file__path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serilialsed_obj = {}
        for key, obj in self.__objects.items():
            serilialsed_obj[key] = obj.to_dict()

        with open(self.__file__path, "w") as json_file:
            json.dump(serilialsed_obj, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        
        if exists(self.__file__path):
            with open(self.__file__path, "r", encoding="utf-8") as json_file:
                deserilialsed_obj = json.load(json_file)
                for key, data_obj in deserilialsed_obj.items():
                    class_name, id_obj = key.split('.')
                    obj_class = globals()[class_name]
                    instance_obj = obj_class(**data_obj)
                    # Store the instance in __objects
                    self.__objects[key] = instance_obj
        