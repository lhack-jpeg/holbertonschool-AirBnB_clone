#!/usr/bin/python3
'''
This module contains the place constructor that inherits from
the basemodel class.
'''

from models.base_model import BaseModel
import models

class Place(BaseModel):
    '''Constructor for Place class.'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    def __init__(self, *args, **kwargs):
        super().__init__()

    def __str__(self):
        """Changes the str return for class"""
        return f"[Place] ({self.id}) {self.__dict__}"
