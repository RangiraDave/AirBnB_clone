#!/usr/bin/python3
"""The codes for creating the console."""

import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand console class definition.\n"""

    prompt = "(hbnb) "
    class_dict = {
            'BaseModel': BaseModel(),
            'FileStorage': FileStorage(),
            'Place': Place(),
            'State': State(),
            'City': City(),
            'Amenity': Amenity(),
            'Review': Review()
            }

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

    def emptyline(self):
        """Function to manage the loop."""

        pass

    def do_create(self, line):
        """
        create class_name command creates new instance of class_name.
        """

        if not line:
            print("** class name missing **")
        elif line not in self.class_dict.keys():
            print("** class dosn't exist **")
        else:
            obj = self.class_dict[line].__class__()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def help_create(self):
        """Function for the create's help."""
        p = "create class_name command "
        p1 = "creates new instance of class_name."
        print("{}{}\n".format(p, p1))

    def do_show(self, line):
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
        elif args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """Helper for show"""

        p = "show class_name instance_id"
        p1 = "to print string represantation of the instance."
        print("{}{}".format(p, p1))

    def do_all(self, line):
        """Function to print string representation of instance."""

        s = line.split(' ')
        if s[0] and s[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            print([str(inst) for inst in storage.all().values()])

    def help_all(self):
        """Helper function for the all command."""

        print("all to print string representation of all instances\n")

    def do_destroy(self, line):
        """
        Function to delete an instance depending on
        the class name and id.
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split(' ')

        if len(args) != 2:
            print("** instance id missing **")
            return

        if args[0] not in self.class_dict.keys():
            print("** class name doesn't exist **")
            return

        key = "{}.{}".format(args[0], args[1])
        cls_instances = storage.all().get(args[0])

        if cls_instances is None or key not in cls_instances:
            print("** no instance found **")
            return
        else:
            del cls_instances[key]
            storage.save()

    def help_destroy(self):
        """Helper function for the destroy command."""

        print("destroy to destroy an instance of class\n")

    def do_update(self, line):
        """Function to update an instance."""

        if not line:
            print("** class name missing **")
            return

        args = line.split(' ')

        if args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        if len(args) == 5:
            cls_inst = storage.all().get(args[1])

            if cls_inst is None or args[1] not in cls_inst:
                print("** no instance found **")
            else:
                at_n = args[2]
                at_v = args[3]
                cls_obj = cls_inst[args[1]]

                try:
                    at_v = type(cls_inst[str(args[1])].__dict__[at_n])(at_v)
                except InvalidFormatError:
                    print("** Invalid format **")

                if at_n not in cls_obj.__dict__:
                    print(f"** attribute '{at_n}' not found in instance **")
                else:
                    cls_obj.__dict__[at_n] = at_v
                    # print('Updated')
                    storage.save()
                    # print('Saved')

    def help_update(self):
        """Helper Function for the update command."""

        print("update <class name> <id> <attribute name> '<attribute value>'")
        print("To update an instance.\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
