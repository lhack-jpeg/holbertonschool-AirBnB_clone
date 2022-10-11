#!/usr/bin/python3
'''
This module contains the user constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    '''Constructor for User class.'''
    def __init__(self):
        super().__init__():
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
