#!/usr/bin/env pyhton3

""" this is the base for all my models"""

from uuid import uuid4
from datetime import datetime
class BaseModel:
    """ this is the base class for all my classes"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at":
                dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                dict[key] = self.updated_at.isoformat()
            else:
                dict[key] = value
        dict["__class__"] = __class__.__name__
        return dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))