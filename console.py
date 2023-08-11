import cmd

"""_summary_"""


class HBNBCommand(cmd.Cmd):
    """_summary_
    Returns:
        _type_: _description_
    """
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
