#!/usr/bin/python3
"""
Definition of baseclass for other classes
"""
import uuid
import datetime


class BaseModel:
    """
    Basemodel for other classes sharing same attr
    Id uniq id for the class
    Created and updated , date records
    """
    def __init__(self, *args, **kwargs):
        """
        id attribute unique for each instance
        created at and updated at , date and time of creation/update
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Prints a string of the attrs Basemodel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update to new datetime when change made
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Dictionary of instances
        each attribute displayed
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
