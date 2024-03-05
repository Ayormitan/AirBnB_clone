#!/usr/bin/python3
"""Define the filestorage class. """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ Represent an abstracted storage
    Attributes:
        __file_path (str): File to save Objects
        __objects (dict): Dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return Dict __objects """
        return FileStorage.__objects
    def new(self, obj):
        """ Return dictionarym __obj"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj
    def save(self):
        """ Serializes object to Json file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
    def reload(self):
        """ Deserialize the Json file """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

