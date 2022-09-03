#!/usr/bin/python3
"""Module for FileStorage class"""


from datetime import datetime
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
        # TODO include the other classes created in task8 and 9
        
        classes = {"BaseModel": BaseModel,
                   "User": User
                   }
        return classes
    def attributes(self):
        """Returns the valid attributes abd their types for classname"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.strptime,
                 "updated_at": datetime.strptime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes