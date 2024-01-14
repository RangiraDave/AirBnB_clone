#!/usr/bin/python3
"""Class Amenity that iniherits from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class definition."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity class constructor."""

        super().__init__(*args, **kwargs)
#    @id.getter
#    def id(self):
#        """Function to return amenity id to use in Place class."""
#        return self.id
