#!/usr/bin/python3
"""
Module for Amenity ORM/FileStorage Class for AirBnB clone - MySQL
"""
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


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
    place_amenities = relationship(
        'Place', secondary=place_amenity,
        back_populates='amenities'
    )
