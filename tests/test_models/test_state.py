#!/usr/bin/python3

"""
description
"""

import datetime, unittest
from models.state import State


class Test_State(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    state = State()
    
    def test_existed_State(self):
        """description"""
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def test_inheritance(self):
        self.assertIsInstance(self.state, State)
    
    def HasAttributes(self):
        """description"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'id'))

    def test_type(self):
        """description"""
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        self.assertIsInstance(self.state.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
