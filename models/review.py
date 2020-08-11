#!/usr/bin/python3
"""
Module for Review ORM/FileStorage Class for AirBnB clone - MySQL
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines all instance attributes for a Review instance/record
       Public class attributes:
       place_id <string>: Place.id = <Class Place> + instance's id
       user_id <string>: User.id = <Class User> + instance's id
       text <string>: User's Review
    """
    place_id = ""
    user_id = ""
    text = ""
