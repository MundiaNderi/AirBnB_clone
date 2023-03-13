#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Initializes the State class

    Attributes:
        name (str) - The name of the state
    """

    name = ""
