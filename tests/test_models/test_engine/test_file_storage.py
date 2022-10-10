#!/usr/bin/python3
''' Cotains tests for the file storage class.'''


import unittest
import pycodestyle
import inspect
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorageDocs(unittest.TestCase):
    '''Test the documentation of the BaseModel Class exists.'''

    @classmethod
    def setUpClass(cls):
        '''Set up testing for function documentation.'''
        cls.file_storage_funcs = inspect.getmembers(
            FileStorage, inspect.isfunction)

    def test_base_model_docs(self):
        '''Check for docs in the module.'''
        module_docs = "models.engine.file_storage".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = FileStorage.__doc__
        self.assertTrue(len(class_docs) >= 1)

        for func in self.file_storage_funcs:
            if len(func[1].__doc__) < 1:
                print(func)
            self.assertTrue(len(func[1].__doc__) >= 1)

class TestFileStorage(unittest.TestCase):
    '''Test the file storage class.'''

    @classmethod
    def setUpClass(cls):
        '''Set up test environment'''
        if os.path.exists("file.json"):
            os.remove("file.json")
        cls.storage = FileStorage()
        cls.storage.reload()
        cls.all_objs = storage.all()
        cls.b1 = BaseModel()

    def test_file_path(self):
        '''Test the file_path exists.'''
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

    def test_file_storage_objects(self):
        '''Test to see the __object attribute.'''
        self.assertTrue(isinstance(self.storage.all(), dict))
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_file_storage_new(self):
        '''Test new method functionality of Filestorage.'''
        my_model = BaseModel()
        my_model.postcode = 2026
        my_model.name = "Ron Swanson"
        my_model.id = '123456'
        self.storage.new(my_model)
        all_objs = self.storage.all()
        key = my_model.__class__.__name__ + '.' + my_model.id
        self.assertIsNotNone(all_objs[key])

    def test_file_storage_save(self):
        '''Test save creates file'''
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_file_storage_reload(self):
        '''test Reload method.'''
        self.storage = FileStorage()
        self.storage.reload()
        self.assertIsNotNone(self.storage.all())
