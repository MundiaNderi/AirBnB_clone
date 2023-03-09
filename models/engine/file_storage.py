#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes
JSON file to instances
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json
from os import path

class FileStorage:
    """Class to hold information and saved instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all objects stored"""

        return self.__objects
