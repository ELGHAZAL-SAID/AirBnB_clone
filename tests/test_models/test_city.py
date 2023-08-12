#!/usr/bin/python3

"""
description
"""

import datetime, unittest
from models.city import City


class Test_City(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    c = City()
    
    def test_existed_City(self):
        """description"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_inheritance(self):
        self.assertIsInstance(self.c, City)
    
    def HasAttributes(self):
        """description"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))
        self.assertTrue(hasattr(self.c, 'id'))

    def test_type(self):
        """description"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)
        self.assertIsInstance(self.c.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
