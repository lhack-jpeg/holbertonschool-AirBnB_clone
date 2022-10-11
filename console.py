#!/usr/bin/python3
"""
This module contains one class HBNBCommand
"""
import cmd
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Interpreter class inheriting from Cmd
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel"]
    int_attrs = ["number_rooms", "number_bathrooms", "max_guest",
                 "price_by_night"]
    float_attrs = ["latitude", "longitude"]

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

    def do_update(self, arg):
        """
        Updates an instance based on class name and class id
        Usage: update <class name> <id> <attribute name> <attribute value>
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

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False

        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value

        if not instance_found:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        if args[2] in self.int_attrs:
            setattr(instance_found, args[2], int(args[3]))
        elif args[2] in self.float_attrs:
            setattr(instance_found, args[2], float(args[3]))
        else:
            setattr(instance_found, args[2], args[3])

        instance_found.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
