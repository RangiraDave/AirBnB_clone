#!/usr/bin/python3
"""The console class 'HBNBCommand'"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand console class definition.\n"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""

        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""

        return True

    def emptyline(self):
        pass

    def postloop(self):
        print


if __name__ == "__main__":
    HBNBCommand().cmdloop()
