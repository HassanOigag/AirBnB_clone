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


class FileStorage():
    """the FileStorate class that stores our data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """save the new object in the objects dict"""
        if type(obj).__name__ == "User":
            obj.first_name = ""
            obj.last_name = ""
            obj.email = ""
            obj.password = ""
        elif type(obj).__name__ == "State":
            obj.name = ""
        elif type(obj).__name__ == "City":
            obj.name = ""
            obj.state_id = ""
        elif type(obj).__name__ == "Amenity":
            obj.name = ""
        elif type(obj).__name__ == "Place":
            obj.name = ""
            obj.user_id = ""
            obj.city_id = ""
            obj.description = ""
            obj.number_rooms = 0
            obj.number_bathrooms = 0
            obj.max_guest = 0
            obj.price_by_night = 0
            obj.latitude = 0.0
            obj.longitude = 0.0
            obj.amenity_ids = []
        elif type(obj).__name__ == "Review":
            obj.place_id = ""
            obj.user_id = ""
            obj.text = ""
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
        dict_of_objects = {}
        try:
            with open(self.__file_path, "r") as f:
                objects_str = f.read()
            if (objects_str):
                json_content = json.loads(objects_str)
                for key, value in json_content.items():
                    class_name = globals()[value.get("__class__")]
                    dict_of_objects[key] = class_name(**value)
            self.__objects = dict_of_objects
        except FileNotFoundError:
            pass
