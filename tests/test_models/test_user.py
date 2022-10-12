#!/usr/bin/python3
''' Cotains tests for the base model class.'''


import unittest
import pycodestyle
import inspect
from models.base_model import BaseModel
from models.user import User


class TestUserModelDocs(unittest.TestCase):
    '''Test the documentation of the User Class exists.'''

    def test_base_model_docs(self):
        '''Check for docs in the module.'''
        module_docs = "models.user".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = User.__doc__
        self.assertTrue(len(class_docs) >= 1)

class TestUserModel(unittest.TestCase):
    '''Test the unit model constructor'''

    @classmethod
    def setUpClass(cls):
        cls.u1 = User()
        cls.u1.email = "test@google.com"
        cls.u1.password = "secret"
        cls.u1.first_name = "ada"
        cls.u1.last_name = "lovelace"
        cls.u2 = User()

    def test_User_class(self):
        '''Check to see class and inheritance.'''
        self.assertTrue(isinstance(self.u1, User))
        self.assertTrue(issubclass(type(self.u1), BaseModel))

    def test_user_cls_attr(self):
        '''Check to see attribute of the User class.'''
        self.assertEqual(len(self.u2.email), 0)
        self.assertEqual(len(self.u2.password), 0)
        self.assertEqual(len(self.u2.first_name), 0)
        self.assertEqual(len(self.u2.last_name), 0)

    def test_user_attr_set(self):
        '''Check to see that user class attr set correctly.'''
        self.assertEqual(self.u1.email, "test@google.com")
        self.assertEqual(self.u1.password, "secret")
        self.assertEqual(self.u1.first_name, "ada")
        self.assertEqual(self.u1.last_name, "lovelace")
