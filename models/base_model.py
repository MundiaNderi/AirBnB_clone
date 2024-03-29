#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initializes arguments for class BaseModel
        Args:
            id - identification number
            *args - arguments
            **kwargs - dictionary arguments
        """

        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a formatted string of classname, id, and dictionary
        contents
        """

        return ("[{}] ({}) {}".format(self.__class__.name__,
                                      self.id, self.__dict__))

    def save(self, name):
        """Saves any new information added to a class instance and
        saves an update time
        """

        self.updated_at = datetime.now()
        self.name = name
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all the contents of a class instance"""

        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
