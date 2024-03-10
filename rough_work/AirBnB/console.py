#!/usr/bin/python3
# command interpreter
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True
    # Aliasing
    do_exit = do_quit

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D (EOF) """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
