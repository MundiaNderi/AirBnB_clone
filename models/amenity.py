#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.bade_model import BaseModel


class Amenity(BaseModel):
    """Initializes the Amenity class
    Attributes:
        name (str) - The name of the amenity
    """

    name = ""
