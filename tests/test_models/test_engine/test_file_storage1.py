#!/usr/bin/python3

"""_summary_
"""

import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest


class Test_FileStorage(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    mod = BaseModel()

    def test_Class_instance(self):
        """_summary_
        """
        self.assertIsInstance(storage, FileStorage)

    def test_storage(self):
        """_summary_
        """
        self.mod.name = 'BaseModel Instance'
        self.mod.save()
        dic = self.mod.to_dict()
        all_objs = storage.all()

        key = dic['__class__'] + "." + dic['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ Test Methods """
        self.mod.my_name = "name"
        self.mod.save()
        bm_dict = self.mod.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        self.mod.my_name = "name"
        self.mod.save()
        bm_dict = self.mod.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "name")

    def test_Attributes(self):
        """_summary_
        """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_save(self):
        """verify if JSON file exists"""
        self.mod.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """test reload Method """
        self.mod.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dob = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dob, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dob[key].to_dict(), value.to_dict())



if __name__ == '__main__':
    unittest.main()