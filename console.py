#!/usr/bin/python3
"""
This module contains one class HBNBCommand
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """
    Interpreter class inheriting from Cmd
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "State", "City",
                  "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Closes the program if Ctrl+d is inputted"""
        print()
        return True

    def emptyline(self):
        """Overrides parent empty line method"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a specified class and prints
        instance's id and saves to file
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class and id
        Usage: show <class name> <class id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_keys = args[0] + "." + args[1]
        all_objs = models.storage.all()

        for key, value in all_objs.items():
            if key == obj_keys:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and class id
        Usage: destroy <class name> <class id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_keys = args[0] + "." + args[1]
        all_objs = models.storage.all()

        for key, value in all_objs.items():
            if key == obj_keys:
                del all_objs[key]
                models.storage.__objects = all_objs
                models.storage.save()
                return

        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints, as a list of strings, the string representation of all
        instances in storage, or all instances of a specified class
        Usage: all - prints every saved object
        Usage: all <class name> - prints every saved object of <class name>
        """
        objs_list = []
        all_objs = models.storage.all()
        args = arg.split()

        if len(args) == 0:
            for key in all_objs:
                objs_list.append(all_objs[key].__str__())
            print(objs_list)
        elif args[0] in self.class_list:
            for key in all_objs:
                if all_objs[key].__class__.__name__ == args[0]:
                    objs_list.append(all_objs[key].__str__())
            print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        '''
        Prints out the count of the classes.
        Usage: <class_name>.count()
        '''
        objs_list = []
        all_objs = models.storage.all()
        args = arg.split()

        for key in all_objs:
            if all_objs[key].__class__.__name__ == args[0]:
                objs_list.append(all_objs[key].__str__())
        print(len(objs_list))

    def do_update(self, arg):
        """
        Updates an instance based on class name and class id
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            elem = args[0] + "." + args[1]
            flag = 0

            for key, value in models.storage.all().items():
                if elem == key:
                    flag = 1
                    break

            if flag == 0:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            setattr(value, args[2], args[3].replace('"', ''))
            models.storage.save()

    def default(self, arg):
        '''This function handles class.cmd() functionality.'''
        args = arg.split('.')
        if len(args) > 1:
            if args[0] in self.class_list:
                if args[1] == 'all()':
                    self.do_all(args[0])
                    return
                if args[1] == 'count()':
                    self.do_count(args[0])
                    return
                cmd_args = args[1].split("(")
                args[1] = cmd_args[0]
                if args[1] == "show" or args[1] == 'destroy':
                    value = cmd_args[1][1:-2]
                    arg_string = f'{args[0]} {value}'
                    if args[1] == 'show':
                        self.do_show(arg_string)
                        return
                    if args[1] == 'destroy':
                        self.do_destroy(arg_string)
                        return
                if args[1] == "update":
                    replacements = [
                        ('"', ""),
                        ("{", ""),
                        ("}", ""),
                        ("'", ""),
                        (')', "")]
                    for old, new in replacements:
                        cmd_args[1] = cmd_args[1].replace(old, new)
                    values = cmd_args[1].split(",")
                    arg_string = f'{args[0]} '
                    for value in values:
                        if value.find(":") != -1:
                            arg_string = f'{args[0]} {values[0]}'
                            dict_entry = value.split(":")
                            for entry in dict_entry:
                                arg_string += f'{entry} '
                            self.do_update(arg_string)
                        else:
                            arg_string += f'{value} '
                    self.do_update(arg_string)
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
