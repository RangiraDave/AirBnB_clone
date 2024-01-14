#!/usr/bin/python3
"""Class View that iniherits from BaseModel."""

from models.base_model import BaseModel
from model.place import Place
from model.user import User


class Review(BaseModel):
    """Class Review is defined here."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Class Review constructor."""

        palce_id = Place.id()
        user_id = User.id()
        super().__init__(*args, **kwargs)
