#!/usr/bin/python3
""" Defination for the HBNB console/interface"""
import cmd
class HBNBCommand (cmd.Cmd):
    """Class defintion for HBNB command line interpreter
    Attributes:
        prompt (str): Command prompt that will be displayed
    """
    prompt = "(hbnb) "
    def emptyline(self):
        """Empty line + ENTER wouldn’t execute anything"""
        pass
    def do_quit(self, arg):
        """Exit the program """
        return True
    def do_EOF(self, arg):
        """Specifies EOF to also quit the program"""
        print("")
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
