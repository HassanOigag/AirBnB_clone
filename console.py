#!/usr/bin/env python3
""" this is a command line interepter for the airbnb clone"""

import cmd
import os

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
    Console().cmdloop()