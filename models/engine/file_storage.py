#!/usr/bin/env python3
""" the file storage class """
import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        obj_dict = obj.to_dict()
        key = f"{obj_dict['__class__']}.{obj_dict['id']}"
        self.__objects[key] = obj_dict
    
    def save(self):
        objects_str = json.dumps(self.__objects)
        with open(self.__file_path, "w") as storage:
            storage.write(objects_str)
    
    def reload(self):
        try:
            with open(self.__file_path, "r") as storage:
                objects_str = storage.read()
            self.__objects = json.loads(objects_str)
        except:
            pass

