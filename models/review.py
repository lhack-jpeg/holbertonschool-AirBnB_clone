#!/usr/bin/python3
'''
This module contains the review constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models


class Review(BaseModel):
    '''Constructor for Review class.'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Changes the str return for class"""
        return f"[Review] ({self.id}) {self.__dict__}"
