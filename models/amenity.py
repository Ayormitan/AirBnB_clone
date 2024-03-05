#!/usr/bin/python3
"""Defines the state class"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Rep a state 

    Attributes:
        name (str): State name
    """
    name = ""
