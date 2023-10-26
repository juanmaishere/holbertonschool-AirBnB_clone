#!/usr/bin/python3
"""
Definition of baseclass for other classes
"""
import json
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return True
    
    def do_create(self, arg):
        arg.split()
        if len(arg) < 2:
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, data):
            args = data.split()
            if len(args) < 2:
                print("** class name missing **")
            if args[2] != "BaseModel":
                print("** class doesn't exist **")
            if len(args) < 3:
                print("** instance id missing **")

            with open("file.json", 'r') as f:
                datax = json.load(f)
            key = f"{args[1]}.{args[2]}"
            if key in datax:
                print(datax)
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
