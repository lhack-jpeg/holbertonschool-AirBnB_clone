#!/usr/bin/python3
''' Cotains tests for the base model class.'''


import unittest
import pycodestyle
import inspect
from models.base_model import BaseModel
from models.state import State


class TestStateModelDocs(unittest.TestCase):
    '''Test the documentation of the State Class.'''

    def test_base_model_docs(self):
        '''Check for docs in the module.'''
        module_docs = "models.state".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = State.__doc__
        self.assertTrue(len(class_docs) >= 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestState(unittest.TestCase):
    '''Test the state class.'''

    @classmethod
    def setUpClass(cls):
        '''Set up test environment'''
        cls.s1 = State()

    def test_state_class(self):
        '''Test type and inheritance of class.'''
        self.assertTrue(isinstance(self.s1, State))
        self.assertTrue(issubclass(type(self.s1), BaseModel))
