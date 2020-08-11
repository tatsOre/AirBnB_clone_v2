#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City, Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
        String(128),
        nullable=False,
    )
    # DBStorage
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    # FileStorage
    else:
        @property
        def cities(self):
            """ Getter method """
            from models import storage
            list_cities = []
            for key, value in storage.all(City).items():
                if self.id == value.state_id:
                    list_cities.append(value)
            return list_cities


