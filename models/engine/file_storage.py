#!/usr/bin/python3
'''This module contains the constructor for the filestorage class.'''


from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    '''This is the constructor for the file storage class.'''
    def __init__(self):
        '''Initalise the Filestoage class'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Add new item to obj dictionary.'''
        if obj is not None:
            obj_class = obj.__class__.__name__ + "." + obj.id
            self.__objects[obj_class] = obj

    def save(self):
        '''Writes the __objects dictionary to file.'''
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

    def reload(self):
        '''Reads the file and deserialise the file. If file doesn't exist do
        nothing.'''
        json_dict = {}
        filename = self.__file_path
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }
        try:
            with open(filename, 'r') as json_file:
                json_dict = json.load(json_file)
                for key, value in json_dict.items():
                    self.__objects[key] = class_dict[value["__class__"]](
                        **value)
        except FileNotFoundError:
            pass
