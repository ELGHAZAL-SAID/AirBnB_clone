#!/usr/bin/python3

"""
description
"""

import datetime
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    user = User()

    def test_existed_User(self):
        """description"""
        self.assertEqual(str(type(self.user)),
                         "<class 'models.user.User'>")

    def test_inheritance(self):
        self.assertIsInstance(self.user, User)

    def HasAttributes(self):
        """description"""
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))
        self.assertTrue(hasattr(self.u, 'id'))

    def test_type(self):
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)
        self.assertIsInstance(self.user.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
