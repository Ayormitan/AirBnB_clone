#!/usr/bin/python3
"""Define the filestorage class. """
import json
from models.base_model import BaseModel
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

