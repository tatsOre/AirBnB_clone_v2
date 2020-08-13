#!/usr/bin/python3
"""
Module for Amenity ORM/FileStorage Class for AirBnB clone - MySQL
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class Amenity(BaseModel, Base):
    """Defines all instance attributes for an Amenity instance/record
        Public class attributes:
        name <string>: Name of the amenity
    """
    __tablename__ = 'amenities'
    name = Column(
        String(128),
        nullable=False,
    )
    if getenv('HBNB_TYPE_STORAGE') == "db":
        place_amenities = relationship(
            'Place', secondary='place_amenity',
            back_populates='amenities')
