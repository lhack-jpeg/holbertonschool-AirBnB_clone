#!/usr/bin/python3
''' Cotains tests for the base model class.'''


import unittest
import pycodestyle
import inspect
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    '''Test the documentation of the BaseModel Class exists.'''

    @classmethod
    def setUpClass(cls):
        '''Set up testing for function documentation.'''
        cls.base_model_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_base_model_docs(self):
        '''Check for docs in the module.'''
        module_docs = "models.base_model".__doc__
        self.assertTrue(len(module_docs) >= 1)

        class_docs = BaseModel.__doc__
        self.assertTrue(len(class_docs) >= 1)

        for func in self.base_model_funcs:
            if len(func[1].__doc__) < 1:
                print(func)
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestBaseModel(unittest.TestCase):
    '''Test the BaseModel Constructor.'''

    @classmethod
    def setUpClass(cls):
        '''Set up objects for testing.'''
        cls.b1 = BaseModel()
        cls.b2 = BaseModel()

    def test_BaseModel_class(self):
        '''Test the class of the BaseModel.'''
        self.assertTrue(isinstance(self.b1, BaseModel))
        self.assertTrue(isinstance(self.b2, BaseModel))

    def test_BaseModel_UUID(self):
        '''Test to ensure the UUID of each instance is unique.
        Note due to the the nature of the randomess of the UUID function,
        this may return a false positive'''
        self.assertTrue(self.b1.id != self.b2.id)

    def test_BaseModel_created_at(self):
        '''Check created_at and updated at equal each other at
        initialisation.'''
        self.assertEqual(self.b1.created_at, self.b1.updated_at)
        self.assertEqual(self.b2.created_at, self.b2.updated_at)

    def test_baseModel_str(self):
        '''Test the return for the __str__ func.'''
        self.assertTrue(isinstance(str(self.b1), str))
        baseModel_str = "[BaseModel] ({:s}) {}".format(
            self.b1.id,
            self.b1.__dict__
        )
        self.assertEqual(str(self.b1), baseModel_str)

    def test_BaseModel_time_format(self):
        '''Check to see created_at and updated_at are are correctly
        formatted.'''
        self.b1.save()
        try:
            self.b1.created_at.isoformat()
            self.b1.created_at.isoformat()
        except Exception as e:
            raise e

    def test_BaseModel_save(self):
        '''Test the save method updates the updated_at attribute.'''
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)
        self.assertTrue(self.b1.created_at < self.b1.updated_at)

    def test_BaseModel_to_dict(self):
        my_dict = self.b2.to_dict()
        self.assertTrue(isinstance(my_dict, dict))
        test_dict_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertEqual(list(my_dict.keys()), test_dict_keys)
