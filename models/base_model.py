#!/usr/bin/python3
""" defines all common attributes/methods for other classes """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel defination for the HBnB projet"""
    def ___init__(self, *args, **kwargs):
        """ Initializes a basemodel.
        Args:
            *args: Unused.
            **Kwargs (dict): Value pair of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()
    def to_dict(self):
        """ dictionary containing all keys/values of __dict__ of the instance"""
        newdict = self.__dict__.copy()
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        newdict["__class__"] = self.__class__.__name__
        return newdict
    def __str__(self):
        """Return the str representation of the basemodel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

