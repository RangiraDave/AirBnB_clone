#!/usr/bin/python3
"""This is a test file for the FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Definition of the TestFileStorage class."""

    def setUp(self):
        """Function set up the environment to be used."""

        self.file_path = 'test_file.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Function to tear down the environment."""

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    """Testing save() and reload methods."""

    def test_with_empty_dictionary(self):
        """Function to test for empty dictionary."""

        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_with_non_empty_dictionary(self):
        """Function to test with some class objects."""

        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 3)

    def test_new_object_addition(self):
        """Testing whether new object can be added to __objects"""

        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)

        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)


if __name__ == "__main__":
    unittest.main()
