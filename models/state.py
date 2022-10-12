#!/usr/bin/python3
'''
This module contains the state constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models

class State(BaseModel):
    '''Constructor for State Class'''
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        '''Changes the str return for class'''
        return f"[State] ({self.id}) {self.__dict__}"
