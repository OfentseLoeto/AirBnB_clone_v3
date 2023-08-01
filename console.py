#!/usr/bin/python3
"""This script build a simple command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to HBNB command interpreter. Type 'help' to list available commands or 'quit' to exit."
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
         """
         Exit the program when EOF (Ctrl+D) is encountered
         """
         return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
