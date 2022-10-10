#!/usr/bin/python3
"""
This module contains one class HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Interpreter class inheriting from Cmd
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Closes the program if Ctrl+d is inputted"""
        print()
        return True

    def emptyline(self):
        """Overrides parent empty line method"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
