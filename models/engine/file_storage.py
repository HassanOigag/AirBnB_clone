#!/usr/bin/env python3
""" the file storage class """
import json

class FileStorage():
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj
    
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

