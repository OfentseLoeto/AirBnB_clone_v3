#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
         """Exit the program gracefully on EOF (Ctrl+D)"""
         print()
         return True

    def emptyline(self):
        """Do nothing when an empty line + ENTER is given"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
