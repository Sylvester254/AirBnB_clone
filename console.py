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

    def do_create(self, input):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if input == "" or input is None:
            print("** class name missing **")
        elif input not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_obj = storage.classes()[input]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, input):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if input == "" or input is None:
            print("** class name missing **")
        else:
            words = input.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
