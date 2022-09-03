#!/usr/bin/python3
"""Entry point for the command interpreter.
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
import json


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

    # HELP COMMANDS

    def help_create(self):
        print("Usage: create <valid class name>")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

    # DO COMMANDS

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

    def do_destroy(self, input):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
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
                    del storage.all()[key]
                    storage.save()

    def do_all(self, input):
        """Prints all string representation of all instances based or not on the class name. 
        """
        if input != "":
            words = input.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                l = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == words[0]]
                print(l)
        else:
            l = [str(obj) for key, obj in storage.all().items()]
            print(l)

    def do_update(self, input):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        if input == "" or input is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, input)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
