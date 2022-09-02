#!/usr/bin/python3
"""Entry point for the command interpreter.
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    
    intro = "Welcome to AirBnB! Type 'help' for more options."
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
    
    def help_quit(self):
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
