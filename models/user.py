#!/usr/bin/python3
'''
This module contains the user constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models

class User(BaseModel):
    '''Constructor for User class.'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Changes the str return for class"""
        return f"[User] ({self.id}) {self.__dict__}"
