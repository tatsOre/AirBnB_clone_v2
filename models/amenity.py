#!/usr/bin/python3
"""
Module for Amenity ORM/FileStorage Class for AirBnB clone - MySQL
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines all instance attributes for an Amenity instance/record
       Public class attributes:
       name <string>: Name of the amenity
    """
    name = ""
