#!/usr/bin/python3

import unittest
from models.state import State


class TestStateModel(unittest.TestCase):
    def setUp(self):
        self.state_model = State()

    def tearDown(self):
        del self.state_model

    def test_instance_creation(self):
        self.assertIsInstance(self.state_model, State)
        self.assertTrue(hasattr(self.state_model, 'id'))
        self.assertTrue(hasattr(self.state_model, 'created_at'))
        self.assertTrue(hasattr(self.state_model, 'updated_at'))
        self.assertTrue(hasattr(self.state_model, 'name'))

    def test_str_repr(self):
        str_repr = str(self.state_model)
        self.assertIn("[State]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("name", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)

    def test_to_dict_method(self):
        state_dict = self.state_model.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertIn('name', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)


if __name__ == '__main__':
    unittest.main()