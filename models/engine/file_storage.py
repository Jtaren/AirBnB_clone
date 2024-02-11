#!/usr/bin/python3
"""
Module containing the FileStorage class
"""

import json
from models import base_model


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            data = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dict_obj = json.load(f)
                for i in dict_obj.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(f"base_model.{cls_name}")(**i))
        except FileNotFoundError:
            pass
