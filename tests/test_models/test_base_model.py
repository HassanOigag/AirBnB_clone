#!/usr/bin/env python3

"""the unittest module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """this is the test of the BaseModel class"""
    def setUp(self):
        self.obj = BaseModel()

    def test_id_exists(self):
        self.assertIsNotNone(self.obj.id)

    def test_id_type_is_str(self):
        self.assertIsInstance(self.obj.id, str)

    def test_create_at_type_is_datetime(self):
        self.assertTrue(isinstance(self.obj.created_at, datetime))

    def test_updated_at_type_is_datetime(self):
        self.assertTrue(isinstance(self.obj.created_at, datetime))

    def test_save(self):
        self.obj.save()
        self.assertNotEqual(self.obj.updated_at, self.obj.created_at)


if __name__ == "__main__":
    unittest.main()
