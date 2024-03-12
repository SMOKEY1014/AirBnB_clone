#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from datetime import datetime
import os


class TestAmenityModel(unittest.TestCase):
    def setUp(self):
        self.amenity_model = Amenity()

    def tearDown(self):
        del self.amenity_model

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity_model, Amenity)
        self.assertTrue(hasattr(self.amenity_model, 'id'))
        self.assertTrue(hasattr(self.amenity_model, 'name'))
        self.assertTrue(hasattr(self.amenity_model, 'created_at'))
        self.assertTrue(hasattr(self.amenity_model, 'updated_at'))

    def test_string_repr(self):
        str_repr = str(self.amenity_model)
        self.assertIn("[Amenity]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("name", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)

    def test_to_dict_method(self):
        amenity_dict = self.amenity_model.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)


if __name__ == '__main__':
    unittest.main()
