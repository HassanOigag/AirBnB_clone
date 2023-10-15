#!/usr/bin/env python3

"""this is the user model resposible for the user stuff"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is user class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
