#!/usr/bin/python3
""" This is the Parent class, the Base Class for this project"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                # if key == '__class__':
                #     continue
                # if key == 'created_at' or key == 'updated_at':
                #     setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                # else:
                #     setattr(self, key, value)
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
