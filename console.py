#!/usr/bin/python3

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

    def do_create(self, type_model):
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.calsses:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
