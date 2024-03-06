#!/usr/bin/python3
# command interpreter
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.users = {} # dict / object initializer

    # basic commands
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

    # Projects commands, CRUD operations.
    def do_create(self, line):
        """ Creates a new user - Syntax : create <id> <name> """
        args = line.split()
        if len(args) == 2:
            id, name = args
            self.users[id] = name
            print(f"User Created - ID: {id} -> Name: {name}")
        else:
            print("Invalid input - use Syntax : create <id> <name>")

    def do_read(self, line):
        """Reads and displays current users- Syntax : read"""
        print("List of users :")
        for id, name in self.users.items():
            print(f"ID: {id} -> Name: {name}")

    def do_update(self, line):
        """Updates users name using their id - Syntax : update <id> <name>"""
        args = line.split()
        if len(args) == 2:
            id, name = args
            if id in self.users:
                self.users[id] = name
                print(f"User updated - ID {id} -> Name: {name}")
            else:
                print(f"User with ID: {id} not found")
        else:
            print("Invalid input - use Syntax : update <id> <name>")

    def do_destroy(self,line):
        """Deletes the user using the id - Syntax : destroy <id>"""
        if line in self.users:
            del self.users[line]
            print(f"User {line} deleted")
        else:
            print(f"User with ID: {line} not found")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
