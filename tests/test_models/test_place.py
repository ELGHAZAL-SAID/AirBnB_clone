#!/usr/bin/python3

"""
description
"""

import datetime, unittest
from models.place import Place
from models.engine.file_storage import FileStorage


class Test_Place(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    p = Place()
    
    def test_existed_Place(self):
        """description"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_inheritance(self):
        self.assertIsInstance(self.p, Place)
    
    def HasAttributes(self):
        """description"""
        att = storage.attributes()["Place"]
        for key in att:
            self.assertTrue(hasattr((self.p, key))

    def test_type(self):
        """description"""
         att = storage.attributes()["Place"]
         for key, value in att.items():
            self.assertEqual(type(getattr(self.p, key, None)), value)



if __name__ == "__main__":
    unittest.main()
