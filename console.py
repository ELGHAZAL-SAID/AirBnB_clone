import cmd

"""_summary_

Returns:
    _type_: _description_
"""


class HBNBCommand(cmd.Cmd):

    """_summary_

    Returns:
        _type_: _description_
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_help(self, line):
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
