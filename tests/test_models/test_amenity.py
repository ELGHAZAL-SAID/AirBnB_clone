#!/usr/bin/python3

"""
description
"""

import datetime, unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    amenity = Amenity()
    
    def test_existed_Amenity(self):
        """description"""
        self.assertEqual(str(type(self.amenity)), "<class 'models.amenity.Amenity'>")

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, Amenity)
    
    def HasAttributes(self):
        """description"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'id'))

    def test_type(self):
        """description"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
