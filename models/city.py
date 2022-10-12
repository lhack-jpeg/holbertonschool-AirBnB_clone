#!/usr/bin/python3
'''
This module contains the city constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models


class City(BaseModel):
    '''Constructor for City class.'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Changes the str return for class"""
        return f"[City] ({self.id}) {self.__dict__}"
