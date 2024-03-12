#!/usr/bin/python3

import unittest
from models.review import Review


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review_model = Review()

    def tearDown(self):
        del self.review_model

    def test_instance_creation(self):
        self.assertIsInstance(self.review_model, Review)
        self.assertTrue(hasattr(self.review_model, 'id'))
        self.assertTrue(hasattr(self.review_model, 'created_at'))
        self.assertTrue(hasattr(self.review_model, 'updated_at'))
        self.assertTrue(hasattr(self.review_model, 'place_id'))
        self.assertTrue(hasattr(self.review_model, 'user_id'))
        self.assertTrue(hasattr(self.review_model, 'text'))

    def test_str_repr(self):
        str_repr = str(self.review_model)
        self.assertIn("[Review]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("user_id", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("place_id", str_repr)
        self.assertIn("text", str_repr)

    def test_to_dict_method(self):
        review_dict = self.review_model.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('text', review_dict)


if __name__ == '__main__':
    unittest.main()
