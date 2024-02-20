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
    def do_create(self, arg):
        """
        Will create class instances ad prints ID.
        """
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()
        def do_show(self, arg):
            """ Usage: show <class> <id>
            Prints the string representation of an instance based on the class name and id.
            """
            arg1 = parse(arg)
            objdict = storage.all()
            if len(arg1) == 0:
                print("** class name missing **")
            elif arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg1) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg1[0],arg1[1]) not in objdict:
                print("** no instance found **")
            else:
                print(objdict["{}.{}".format(arg1[0], arg1[1])])
if __name__ == '__main__':
    HBNBCommand().cmdloop()
