#!/usr/bin/env python3

""" the file storage class """


import json
from ..base_model import BaseModel
from ..amenity import Amenity
from ..user import User
from ..city import City
from ..state import State
from ..place import Place
from ..review import Review


class FileStorage:
    """the FileStorate class that stores our data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """save the new object in the objects dict"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """save the objects dict to the json file"""
        dict_of_objects = {}
        for key, value in self.__objects.items():
            dict_of_objects[key] = value.to_dict()
        objects_str = json.dumps(dict_of_objects)
        with open(self.__file_path, "w") as f:
            f.write(objects_str)

    def reload(self):
        """reads from the json file and stores it in object dict"""
        try:
            with open(self.__file_path, "r") as f:
                objects_str = f.read()
            if (objects_str):
                json_content = json.loads(objects_str)
                for key, value in json_content.items():
                    class_name = globals()[value.get("__class__")]
                    self.__objects[key] = class_name(**value)
        except (FileNotFoundError, FileExistsError):
            pass
