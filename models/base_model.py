#!/usr/bin/python3
""" This is the Parent class, the Base Class for this project"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
            
                    if key == 'created_at' or key == 'updated_at':
                        # Convert string to datetime object
                        value = setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.save()
        # storage.new(self)

        if self.id is None:
            storage.new(self)
        # return self.updated_at
    
    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj