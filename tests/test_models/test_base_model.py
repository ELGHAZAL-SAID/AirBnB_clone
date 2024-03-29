#!/usr/bin/python3

""" models of unittests """

import unittest
import os
import datetime


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ method tests """

    mod = BaseModel()

    def test_BaseModel(self):
        """ Test attributest values of BaseModel instance """

        self.mod.name = "model"
        self.mod.num = 89
        self.mod.save()
        mod_json = self.mod.to_dict()

        self.assertEqual(self.mod.name, mod_json['name'])
        self.assertEqual(self.mod.num, mod_json['num'])
        self.assertEqual('BaseModel', mod_json['__class__'])
        self.assertEqual(self.mod.id, mod_json['id'])

    def test_save(self):
        """ checks if save method updates the public instances """
        self.mod.first_name = "name"
        self.mod.save()

        self.assertIsInstance(self.mod.id, str)
        self.assertIsInstance(self.mod.created_at, datetime.datetime)
        self. assertIsInstance(self.mod.updated_at, datetime.datetime)

        dict_one = self.mod.to_dict()

        self.mod.first_name = "otherName"
        self.mod.save()
        dict_two = self.mod.to_dict()

        self.assertEqual(dict_one['created_at'], dict_two['created_at'])
        self.assertNotEqual(dict_one['updated_at'], dict_two['updated_at'])


if __name__ == '__main__':
    unittest.main()
