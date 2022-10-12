#!/usr/bin/python3
"""
This module contains the super class BaseModel
"""
import uuid
from datetime import datetime
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    This is the base model class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_time = datetime.strptime(value, time)
                    setattr(self, key, date_time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a readable string of an instance
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public attribute 'updated_at' with current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of '__dict__' of an instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
