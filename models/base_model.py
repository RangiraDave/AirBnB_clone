#!/usr/bin/python3
"""
    The base class 'BaseModel'.
"""
import uuid
from datetime import datetime


class BaseModel():
    """
        Class that defines attributes/methods for other classes.
    """

    def __init__(self):
        """The initiator function."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def name(self, name):
        """Function to set and return client name."""

        self.name = name
        return self.name

    def my_number(self, my_number):
        """Function to return set and return client number."""

        self.my_number = my_number
        return my_number

    def __str__(self):
        """Function to return the desired string representation."""

        name = __class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Function to update the updated_at with current time."""

        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        Function to return a dictionary containing all
        keys/values of __dict__ of instances
        """

        u_str = self.updated_at.isoformat()
        c_str = self.created_at.isoformat()
        __dict__ = {
                'my_number': self.my_number,
                'name': self.name,
                '__class__': self.__class__.__name__,
                'updated_at': u_str,
                'id': self.id,
                'created_at': c_str
                }
        return __dict__
