#!/usr/bin/env python3
""" this is a command line interepter for the airbnb clone"""

import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from pprint import pprint


def cast(str):
    """catsts the input string to the its actual data type"""
    if str.isdigit():
        return int(str)
    else:
        try:
            res = float(str)
            return res
        except ValueError:
            return str


class HBNBCommand(cmd.Cmd):
    """Simple airbnb console."""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "City", "Amenity", "Review"]

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
        """Creates a new instance
        of BaseModel, saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = globals()[line]
            new = class_name()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            id = f"{args[0]}.{args[1]}"
            instance_dict = storage.all().get(id)
            if not instance_dict:
                print("** no instance found **")
            else:
                class_name = globals()[args[0]]
                obj = class_name(**instance_dict)
                print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on
        the class name and id (save the change into the JSON file)"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
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
        """Prints all string
        representation of all instances based or not on the class name"""
        instances = []
        if line not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            for value in all_objects.values():
                if value["__class__"] == line:
                    class_name = globals()[line]
                    obj = class_name(**value)
                    instances.append(obj.__str__())
            print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into
        the JSON file)."""
        error = 0
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            error = 1
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                error = 1
            else:
                print("** instance id missing **")
                error = 1
        else:
            all_objs = storage.all()
            id = f"{args[0]}.{args[1]}"
            instance_dict = all_objs.get(id)
            if not instance_dict:
                print("** no instance found **")
                error = 1
        if error:
            return
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            attr_name = args[2]
            attr_value = args[3]
            instance_dict[attr_name] = cast(attr_value)
            class_name = globals()[args[0]]
            obj = class_name(**instance_dict)
            obj.save()

    def emptyline(self):
        """if no command entered it displays a new prompt"""
        pass


if __name__ == "__main__":
    """this is the main"""
    HBNBCommand().cmdloop()
