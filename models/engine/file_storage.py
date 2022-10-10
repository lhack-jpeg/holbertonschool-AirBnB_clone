#!/usr/bin/python3
'''This module contains the constructor for the filestorage class.'''


from models.base_model import BaseModel
import json


class FileStorage:
    '''This is the constructor for the file storage class.'''
    def __init__(self):
        '''Initalise the Filestoage class'''
        self.__file_path = dope_file_path_name.json
        self.__objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Add new item to obj dictionary.'''
        if obj is not None:
            obj_class = obj.__class__.__name__
            self.__objects[obj_class] = obj.id

    def save(self):
        '''Writes the __objects dictionary to file.'''
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            json.dumps(self.__filepath, self.all)

    def reload(self):
        '''Reads the file and deserialise the file. If file doesn't exist do
        nothing.'''

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                json.loads(self.__filepath)
        except Exception:
            pass
