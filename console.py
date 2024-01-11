#!/usr/bin/python3
"""The console class 'HBNBCommand'"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand console class definition.\n"""

    prompt = "(hbnb) "
    class_dict = {'BaseModel': BaseModel(), 'FileStorage': FileStorage}

    def do_quit(self, line):
        """Quit command to exit the program\n"""

        return True

    def help_quit(self):
        """Function for the quit help.\n"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program\n"""

        return True

    def help_EOF(self):
        """Function for EOF's help."""
        print("EOF command to exit the program\n")

    def postloop(self):
        """Function to manage the loop."""
        print

    def do_create(self, line):
        """
        create class_name command creates new instance of class_name.
        """

        if not line:
            print("** class name missing **")
        elif line not in self.class_dict.keys():
            print("** class dosn't exist **")
        else:
            obj = BaseModel()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def help_create(self):
        """Function for the create's help."""
        p = "create class_name command "
        p1 = "creates new instance of class_name."
        print("{}{}\n".format(p, p1))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
