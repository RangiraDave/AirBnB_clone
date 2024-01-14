#!/usr/bin/python3
"""Class City that iniherits from BaseModel class."""

from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """City class is defined here."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City class constructor."""

#        self.state_id = State.id()
        super().__init__(*args, **kwargs)
#    @id.getter
#    def id(self):
#        """Function to return city id to use in Place class."""
#        return self.id
