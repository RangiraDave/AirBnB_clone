#!/usr/bin/python3
"""
Script to create FileStorage class.
"""
import json


class FileStorage():
    """
    Class to serialize and deserialize the dictionary in a file
    """

    def __init__(self):
        """FileStorage constructor"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Function to return __objects dictionary."""

        return self.__objects

    def new(self, obj):
        """
        Function to set in __objects the obj
        with key '<obj class name>.id'
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Function to serialize __objects to __file_path JSON file
        """

        t = self.__objects.items()
        serialized_obj = {key: obj.to_dict() for key, obj in t}
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(serialized_obj, f, default=str)
        return f

    def reload(self):
        """
        Function to deserialize __file_path JSON to __objects."""

        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                data = f.read()
                if data:
                    # f.seek(0)
                    d = json.loads(data)

                    from models.base_model import BaseModel
                    from models.user import User

                    c = {
                            'BaseModel': BaseModel,
                            'User': User,
                            'Place': Place,
                            'State': State,
                            'City': City,
                            'Amenity': Amenity,
                            'Review': Review
                            }
                    cls = '__class__'
                    t = {k: c.get(d[k][cls], c.keys())(**d[k]) for k in d}
                    self.__objects = t
        except FileNotFoundError:
            pass
