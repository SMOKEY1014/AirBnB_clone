#!/usr/bin/python3
"""
Module for the Base Class
- Public instance attributes
    - id
    - created_at
    - updated_at
- Public instance methods
    - save(self) - updates the updated_at attribute
    - to_dict(self) - returns dictionary
- __str__ method to print
"""

from datetime import datetime
import uuid
# from . import storage
import models


class BaseModel:

    """
    This is the base model class
    It is an abstract class from which all other classes would inherit from
    """
    def __init__(self, *args, **kwargs):

        """
        Initialiazes new instance of BaseModel.

        Args:
            *args: Unused positional arguments
            **kwargs: Dictionary representation of an instance.

        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attr name
            Convert datetime to datetime objects

        Otherwise:
            Create id and created_at values as initially done
        """
        if kwargs:
            if '__class__' in kwargs:
                # Remove '__class__' from the dictionary
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the object class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute and saves the object to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()  # Delegate saving to storage
        models.storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary containing key/value of __dict__ for an instance
        """
        exclude = ['name', 'my_number']
        obj_dict = {key: value for key,
                    value in self.__dict__.items() if key not in exclude}
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
