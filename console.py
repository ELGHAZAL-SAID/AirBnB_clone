#!/usr/bin/pythob3

import cmd
from models.base_model import BaseModel


"""_summary_"""


class HBNBCommand(cmd.Cmd):
    """_summary_
    Returns:
        _type_: _description_
    """
     calsses = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = globals()[arg]
        except KeyError:
            print("** class doesn't exist **")
            return

        objt = cls()
        objt.save()
        print(objt.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
