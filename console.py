import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_help(self, line):
        cmd.Cmd.do_help(slef, line)

    def emptyline(self):
        pass

    if __name__ == "__main__":
        HBNBCommnad().cmdloo()
