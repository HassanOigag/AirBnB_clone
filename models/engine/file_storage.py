#!/usr/bin/env python3

""" the file storage class """

import json


class FileStorage():
    """the FileStorate class that stores our data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the stored objects"""
        return self.__objects

    def new(self, obj):
        """save the new object in the objects dict"""
        obj_dict = obj.to_dict()
        if type(obj).__name__ == "User":
            obj_dict["first_name"] = ""
            obj_dict["last_name"] = ""
            obj_dict["email"] = ""
            obj_dict["password"] = ""
        elif type(obj).__name__ == "State":
            obj_dict["name"] = ""
        elif type(obj).__name__ == "City":
            obj_dict["name"] = ""
            obj_dict["state_id"] = ""
        elif type(obj).__name__ == "Amenity":
            obj_dict["name"] = ""
        elif type(obj).__name__ == "Place":
            obj_dict["name"] = ""
            obj_dict["user_id"] = ""
            obj_dict["city_id"] = ""
            obj_dict["description"] = ""
            obj_dict["number_rooms"] = 0
            obj_dict["number_bathrooms"] = 0
            obj_dict["max_guest"] = 0
            obj_dict["price_by_night"] = 0
            obj_dict["latitude"] = 0.0
            obj_dict["longitude"] = 0.0
            obj_dict["amenity_ids"] = []
        elif type(obj).__name__ == "Review":
            obj_dict["place_id"] = ""
            obj_dict["user_id"] = ""
            obj_dict["text"] = ""
        key = f"{obj_dict['__class__']}.{obj_dict['id']}"
        self.__objects[key] = obj_dict

    def save(self):
        """save the objects dict to the json file"""
        objects_str = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(objects_str)

    def reload(self):
        """reads from the json file and stores it in object dict"""
        try:
            with open(self.__file_path, "r") as f:
                objects_str = f.read()
            self.__objects = json.loads(objects_str)
        except FileNotFoundError:
            pass
