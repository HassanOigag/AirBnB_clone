#!/usr/bin/env pyhton3

""" this is the base for all my models"""
from pprint import pprint
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ this is the base class for all my classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
            
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

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
