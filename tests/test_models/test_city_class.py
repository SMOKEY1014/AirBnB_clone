#!/usr/bin/python3

import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city_model = City()

    def tearDown(self):
        del self.city_model

    def test_instance_creation(self):
        self.assertIsInstance(self.city_model, City)
        self.assertTrue(hasattr(self.city_model, 'id'))
        self.assertTrue(hasattr(self.city_model, 'updated_at'))
        self.assertTrue(hasattr(self.city_model, 'created_at'))
        self.assertTrue(hasattr(self.city_model, 'name'))
        self.assertTrue(hasattr(self.city_model, 'state_id'))

    def test_string_repr(self):
        str_repr = str(self.city_model)
        self.assertIn("[City]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("name", str_repr)
        self.assertIn("state_id", str_repr)

    def test_to_dict_method(self):
        city_dict = self.city_model.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('state_id', city_dict)


if __name__ == '__main__':
    unittest.main()