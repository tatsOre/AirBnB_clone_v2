#!/usr/bin/python3
"""
Module for BaseModel ORM/FileStorage Class for AirBnB clone - MySQL
"""
import uuid
import models
from datetime import datetime
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """Defines the Base model and class attributes for all derived classes
       Public instance attributes:
    id <string>: Random/unique ID assigned when an instance is created
    created_at <datetime object>: current datetime when an instance is created
    updated_at <datetime object>: current datetime when an instance is updated
    """
    id = Column(
        String(60),
        nullable=False,
        primary_key=True,
    )
    created_at = Column(
        DateTime, default=datetime.utcnow(),
        nullable=False,
    )
    updated_at = Column(
        DateTime, default=datetime.utcnow(),
        nullable=False,
    )

    def __init__(self, *args, **kwargs):
        """Constructor - Sets attributes to all future instances from:
        Args:
            *args: Tuple that contains all attributes
            **kwargs: dictionary that contains all attributes by key/value args
                (Note __class__ from kwargs is not added as an attribute and
                created_at and updated_at are converted into datetime object)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance"""
        dictionary = self.to_dict()
        del dictionary["__class__"]
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ Delete the current instance from storage. """
        models.storage.delete(self)
