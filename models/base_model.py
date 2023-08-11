#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():

    """BaseModel class that defines common attributes/methods"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation in the format:
            "[<class name>] (<self.id>) <self.__dict__>"
        """
        return ("[{}] ({}) {}"
                "".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary representation.

        Returns:
            dict: Dictionary containing instance attributes.
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
