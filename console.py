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
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
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
        Prints the string representation of an
        instance based on the class name and id
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
        """Deletes an instance based on the
        class name and id (save the change into the JSON file).
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
        """Prints all string representation of
        all instances based or not on the class
        name.
        """
        if input != "":
            words = input.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                line = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(line)
        else:
            line = [str(obj) for key, obj in storage.all().items()]
            print(line)

    def do_update(self, input):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
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

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(<id>, <attribute name>, <attribute value>) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(<id>, <attribute name>, <attribute value>) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
