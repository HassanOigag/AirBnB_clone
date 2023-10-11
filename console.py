#!/usr/bin/env python3
""" this is a command line interepter for the airbnb clone"""

import cmd
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class Console(cmd.Cmd):
    """Simple airbnb console."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ quits the programm """
        return True

    def do_quit(self, line):
        """ exits the programm """
        return True

    def do_clear(self, line):
        """ clears the console """
        os.system("clear")

    def emptyline(self):
        """ if no command entered it display a new prompt"""
        pass

if __name__ == "__main__":
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)