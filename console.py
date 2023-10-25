#!/usr/bin/python3
"""
Definition of baseclass for other classes
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()