#!/usr/bin/python3
"""
    Tester for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
        Class that is used to auto test the
        BaseModel functionalities.
    """

    def test_id(self):
        """Testing whether id is being created."""

        obj = BaseModel()
        self.assertTrue(obj.id)

    def test_name(self):
        """Testing whether name can be created."""

        obj = BaseModel
        obj.name = "Dave"
        self.assertEqual(obj.name, "Dave")

    def test_my_number(self):
        """Testing whether my_number can be created."""

        obj = BaseModel()
        obj.my_number = 78898965
        self.assertEqual(obj.my_number, 78898965)

    def test_CreatedTime(self):
        """Testing the time of creation."""

        obj = BaseModel()
        self.assertTrue(obj.created_at)

    def test_UpdatedTime(self):
        """
            Testing whether time is updated when save
            attribute is called.
        """

        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_dictionary(self):
        """Testing whether dictionary is being created."""

        obj = BaseModel()
        dic = obj.to_dict()
        self.assertEqual(str(type(dic)), "<class 'dict'>")

    def test_Kwargs(self):
        """Testing kwargs holding dict representation"""

        obj = BaseModel()
        obj.name = "Dave"
        json = obj.to_dict()
        obj2 = BaseModel(**json)
        self.assertEqual(obj2.name, obj.name)
