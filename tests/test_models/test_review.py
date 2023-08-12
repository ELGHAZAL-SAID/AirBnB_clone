#!/usr/bin/python3

"""
description
"""

import datetime, unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    r = Review()
    
    def test_existed_Review(self):
        """description"""
        self.assertEqual(str(type(self.r)), "<class 'models.review.Review'>")

    def test_inheritance(self):
        self.assertIsInstance(self.r, Review)
    
    def HasAttributes(self):
        """description"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))
        self.assertTrue(hasattr(self.r, 'id'))

    def test_type(self):
        """description"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)
        self.assertIsInstance(self.r.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
