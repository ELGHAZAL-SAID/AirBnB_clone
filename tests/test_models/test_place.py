#!/usr/bin/python3

"""
description
"""

import datetime
import unittest
from models.place import Place
from models import storage
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
            self.assertTrue(hasattr((self.p, key)))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        attributes = [
            ('city_id', str),
            ('user_id', str),
            ('name', str),
            ('description', str),
            ('number_rooms', int),
            ('number_bathrooms', int),
            ('max_guest', int),
            ('price_by_night', int),
            ('latitude', float),
            ('longitude', float),
            ('amenity_ids', list),
            ('id', str),
            ('created_at', datetime.datetime),
            ('updated_at', datetime.datetime)
        ]

        for attr_name, expected_type in attributes:
            with self.subTest(attr_name=attr_name):
                attr_value = getattr(self.p, attr_name)
                self.assertIsInstance(attr_value, expected_type)


if __name__ == "__main__":
    unittest.main()
