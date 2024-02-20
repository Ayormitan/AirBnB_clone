#!/usr/bin/python3
""" class User """
from models.base_model import BaseModel

class User(BaseModel):
    """ Represent a user.
    Attributes:
        email (str): The email of user.
        password (str): Users password.
        first_name (str): Users first name
        last_name (str): User last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
