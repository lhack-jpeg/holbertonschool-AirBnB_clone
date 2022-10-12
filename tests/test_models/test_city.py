#!/usr/bin/python3
''' Cotains tests for the base model class.'''


import unittest
import pycodestyle
import inspect
from models.base_model import BaseModel
from models.city import City


class TestCityModelDocs(unittest.TestCase):
    '''Test the documentation of the City Class.'''

    def test_base_model_docs(self):
        '''Check for docs in the module.'''
        module_docs = "models.city".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = City.__doc__
        self.assertTrue(len(class_docs) >= 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestCityModel(unittest.TestCase):
    '''Test City model.'''

    @classmethod
    def setUpClass(cls):
        '''Set up test environment'''
        cls.c1 = City()

    def test_state_class(self):
        '''Test type and inheritance of class.'''
        self.assertTrue(isinstance(self.c1, City))
        self.assertTrue(issubclass(type(self.c1), BaseModel))
