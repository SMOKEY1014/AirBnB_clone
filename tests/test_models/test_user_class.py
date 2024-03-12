#!/usr/bin/python3

import unittest
from models import user


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user_model = user.User()

    def tearDown(self):
        del self.user_model

    def test_instance_creation(self):
        self.assertIsInstance(self.user_model, user.User)
        self.assertTrue(hasattr(self.user_model, 'id'))
        self.assertTrue(hasattr(self.user_model, 'created_at'))
        self.assertTrue(hasattr(self.user_model, 'updated_at'))
        self.assertTrue(hasattr(self.user_model, 'email'))
        self.assertTrue(hasattr(self.user_model, 'password'))
        self.assertTrue(hasattr(self.user_model, 'first_name'))
        self.assertTrue(hasattr(self.user_model, 'last_name'))

    def test_str_rep(self):
        str_rep = str(self.user_model)
        self.assertIn("[User]", str_rep)
        self.assertIn("id", str_rep)
        self.assertIn("created_at", str_rep)
        self.assertIn("updated_at", str_rep)
        self.assertIn("password", str_rep)
        self.assertIn("email", str_rep)
        self.assertIn("last_name", str_rep)
        self.assertIn("first_name", str_rep)

    def test_to_dict_func(self):
        user_dict = self.user_model.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('first_name', user_dict)


if __name__ == '__main__':
    unittest.main()
