#!/usr/bin/python3
# command interpreter
import cmd
import json

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
        self.save()

    def do_read(self, line):
        """Reads and displays current users- Syntax : read"""
        self.load()
        print("List of users :")
        for id, name in self.users.items():
            print(f"ID: {id} -> Name: {name}")

    def do_update(self, line):
        """Updates users name using their id - Syntax : update <id> <name>"""
        self.load()
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
        self.save()

    def do_destroy(self,id):
        """Deletes the user using the id - Syntax : destroy <id>"""
        # must check if id is an integer, else return an error
        if id in self.users:
            del self.users[id]
            print(f"User ID:{id} deleted")
        else:
            print(f"User with ID: {id} not found")
        self.save()

    def save(self):
        """Saves data into a json file"""
        with open("user_data.json","w") as json_file:
            json.dump(self.users, json_file)

    def load(self):
        """Loads data from the json file"""
        with open("user_data.json", "r") as json_file:
            self.users = json.load(json_file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
