#!/usr/bin/python3
"""State class that iniherits from BaseModel class."""

from models.base_model import BaseModel


class State(BaseModel):
    """State class is defined here."""

    name = ""

    def __init__(self, *args, **kwargs):
        """State class constructor."""

        super().__init__(*args, **kwargs)

    @id.getter
    def id(self):
        """Function to return state id"""

        return self.id
