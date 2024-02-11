#!/usr/bin/python3
"""Module containing the FileStorage class.

This module contains the FileStorage class which
serializes instances to a JSON file
and deserializes JSON files to instances.
"""

import json
from models import base_model


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): The file path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to be added to __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(f"base_model.{cls_name}")(**o))
        except FileNotFoundError:
            pass
