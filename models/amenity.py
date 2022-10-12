#!/usr/bin/python3
'''
This module contains the amenity constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models

class Amenity(BaseModel):
    '''Constructor for Amenity class.'''
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Changes the str return for class"""
        return f"[Amenity] ({self.id}) {self.__dict__}"
