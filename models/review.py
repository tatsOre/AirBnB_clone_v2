#!/usr/bin/python3
"""
Module for Review ORM/FileStorage Class for AirBnB clone - MySQL
"""
from models.base_model import BaseModel
from sqlalchemy import String, Column, ForeignKey


class Review(BaseModel):
    """Defines all instance attributes for a Review instance/record
       Public class attributes:
       place_id <string>: Place.id = <Class Place> + instance's id
       user_id <string>: User.id = <Class User> + instance's id
       text <string>: User's Review
    """
    __tablename__ = 'reviews'
    text = Column(
       String(1024),
       nullable=False,
    )
    place_id = Column(
       String(60),
       ForeignKey('places.id'),
       nullable=False,
    )
    user_id = Column(
       String(60),
       ForeignKey('users.id'),
       nullable=False,
    )
