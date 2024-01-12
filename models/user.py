#!/usr/bin/python3
"""Class User that inherits from the BaseModel class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User definition."""

    def __init__(self, *args, **kwargs):
        """Class User constructor."""

        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    @property
    def email(self):
        """Function to initialize user email."""

        return self.__email

    @email.setter
    def email(self, value):
        """Function to set the value of email."""

        self.__email = value

    @property
    def password(self):
        """Function to set the user password."""

        return self.__password

    @password.setter
    def password(self, value):
        """Function to set the value of password."""

        self.__password = value

    @property
    def first_name(self):
        """Function to set the user first name."""

        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """Function to set the value of first_name"""

        self.__first_name = value

    @property
    def last_name(self):
        """Function to set the value of the user's last name."""

        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """Function to set value of last_name."""

        self.__last_name = value
