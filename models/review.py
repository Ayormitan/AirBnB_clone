#!/usr/bin/python3
"""Defines the state class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """ Rep a state 

    Attributes:
        place_id = emty string
        user_id = empty string
        text (str): Statetext
    """
    place_id = ""
    user_id = ""
    text = ""
