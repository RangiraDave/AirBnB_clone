#!/usr/bin/python3
"""Place class that iniherits from BaseModel."""

from models.base_model import BaseModel
# from models.city import City
# from models.user import User
# from models.amenity import Amenity


class Place(BaseModel):
    """Place class constructor."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Class Place constructor."""

        super().__init__(*args, **kwargs)
#        city_id = City.id()
#        user_id = User.id()
#        amenity_id += Amenity.id()
#        @id.getter
#        def id(self):
#            """Function to return place id to use in Review class"""
#            return self.id
