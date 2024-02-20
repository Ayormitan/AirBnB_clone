#!/usr/bin/python3
""" Defination for the HBNB console/interface"""
import cmd
import re
from models import storage
from shlex import split
class HBNBCommand (cmd.Cmd):
    """Class defintion for HBNB command line interpreter
    Attributes:
        prompt (str): Command prompt that will be displayed
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
    }
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
    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        arg1 = parse(arg)
        objdict = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg1[0], arg1[1])]
            storage.save()
    def do_all(self, arg):
        """Usage: All <class>()
         Prints all string representation of all instances
        """
        arg1 = parse(arg)
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg1) == 0:
                    obj1.append(obj.__str__())
            print(obj1)
    def do_updtate(self, arg):
        """Usage <class> <id> <attribute_name> <attribute_value> """
        arg1 = parse(arg)
        objdict = storage.all()
        if len(arg1) == 0:
            print("** Class name missing **")
            return False
        if arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg1) == 4:
            obj = objdict["{}.{}".format(arg1[0], arg1[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg1[2]])
                obj.__dict__[arg1[2]] == valtype(arg1[3])
            else:
                obj.__dict__[arg1[2]] = arg1[3]
        elif type(eval(arg1[2])) == dict:
            obj = objdict["{}.{}".format(arg1[0], arg1[1])]
            for k, v in eval(arg1[2]).item():
                if (k in ibj.__class__.__dict__.key() and type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret1 = [i.strip(",") for i in lexer]
            ret1.append(brackets.group())
            return ret1
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret1 = [i.strip(",") for i in lexer]
        ret1.append(curly_braces.group())
        return ret1


if __name__ == '__main__':
    HBNBCommand().cmdloop()
