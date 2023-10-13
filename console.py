#!/usr/bin/env python3
""" this is a command line interepter for the airbnb clone"""

import cmd
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple airbnb console."""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command quits the programm"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_clear(self, line):
        """clears the console"""
        os.system("clear")
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            id = f"{args[0]}.{args[1]}"
            instance_dict = storage.all().get(id)
            if not instance_dict:
                print("** no instance found **")
            else:
                obj = BaseModel(**instance_dict)
                print(obj)
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            id = f"{args[0]}.{args[1]}"
            instance_dict = all_objs.get(id)
            if not instance_dict:
                print("** no instance found **")
            else:
                del all_objs[id]
                storage.save()

    def do_all(self, line):
        objs_list = []
        if line not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            for value in all_objects.values():
                obj = BaseModel(**value)
                objs_list.append(obj.__str__())
            print(objs_list)

    def do_update(self, line):
        pass

    def emptyline(self):
        """if no command entered it displays a new prompt"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
    # all_objs = storage.all()
    # print("-- Reloaded objects --")
    # for obj_id in all_objs.keys():
    #     obj = all_objs[obj_id]
    #     print(obj)

    # print("-- Create a new object --")
    # my_model = BaseModel()
    # my_model.name = "My_First_Model"
    # my_model.my_number = 89
    # my_model.save()
    # print(my_model)