#!/usr/bin/python3
"""Module for FileStorage class"""


import json
import os


class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns __objects dictionary."""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as myfile:
            dictionary = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dictionary, myfile)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as myfile:
            dictionary = json.load(myfile)
            dictionary = {k: self.classes()[v["__class__"]](**v) for k,v in dictionary.items()}
            FileStorage.__objects = dictionary

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User
                   }
        return classes
