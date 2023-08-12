#!/usr/bin/python3

import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User

import shlex

"""_summary_"""


class HBNBCommand(cmd.Cmd):
    """_summary_
    Returns:
        _type_: _description_
    """
    cal = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']

    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, type_model):
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.cal:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, type_):
        if not type_:
            print("** class name missing **")
            return

        type_ = type_.split(' ')

        if type_[0] not in HBNBCommand.cal:
            print("** class doesn't exist **")
        elif len(type_) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(type_[0], type_[1])
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, type_):
        if not type_:
            print("** class name missing **")
            return

        type_ = type_.split(' ')

        if type_[0] not in HBNBCommand.cal:
            print("** class doesn't exist **")
        elif len(type_) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(type_[0], type_[1])
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
                return
            else:
                print("** no instance found **")

    def do_all(self, type_):
        if not type_:
            print("** class name missing **")
            return

        if type_ not in HBNBCommand.cal:
            print("** class doesn't exist **")
        else:
            for obj_key, value in storage.all().items():
                if type_ == value.__class__.__name__:
                    instance_list = [value.__str__()]
                    print(instance_list)

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        string = ''

        for argv in arg.split(','):
            string = string + argv

        args = shlex.split(string)

        if args[0] not in HBNBCommand.cal:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.save()
                return
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
