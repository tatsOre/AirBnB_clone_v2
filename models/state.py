#!/usr/bin/python3
"""
Module for State ORM/FileStorage Class for AirBnB clone - MySQL
"""
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Defines all instance attributes for a State instance/record"""
    __tablename__ = 'states'
    name = Column(
        String(128),
        nullable=False,
    )
    cities = relationship('City', backref='state', cascade='all, delete')
    # FileStorage
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns list of City instances with state_id"""
            from models import storage
            from models.city import City
            list_cities = []
            for key, value in storage.all(City).items():
                if self.id == value.state_id:
                    list_cities.append(value)
            return list_cities
