#!usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Initializes the city class

    Attributes:
        state_id (str) - refers to the State.id
        name (str) - The name of the city
    """

    state_id = ""
    name = ""
