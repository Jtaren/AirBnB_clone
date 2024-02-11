#!/usr/bin/python3
"""Defines a parent class Basemodel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Class Basemodel is a parent class that defines all common
    attributes and methods for other classes

    Methods:
        -__init__(): initialises the self when called
        -__str__(): prints the class name
        -save(): updates and saves the instance
        -to_dict(): returns a dictionary representation of the instance
    """

    def __init__(self, *args, **kwargs):
        """Initialises the instance attributes"""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a tring representaion of the instance"""
        return f"{[self.__class__.__name__]}, {self.id}, {self.__dict__}"

    def save(self):
        """Updates and saves the instance when updated"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Generates a dictionary representation of an instance.

        Returns:
            A dictionary containing key-value pairs
            of the instance attributes
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
