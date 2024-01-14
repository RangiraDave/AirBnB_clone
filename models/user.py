#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Class User definition."""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    @id.getter
#    def id(self):
#        """Function to return id to use in Place class."""
#        return self.id

    def to_dict(self):
        """
        Function to return dictionary representation of the user
        """

        e = self.email
        p = self.password
        f1 = self.first_name
        la = self.last_name
        l_n = 'last_name'
        f_n = 'first_name'

        base_dict = super().to_dict()
        user_dict = {
                'email': e,
                'password': p,
                f'{f_n}': f1,
                f'{l_n}': la,
                **base_dict
                }

        return user_dict
