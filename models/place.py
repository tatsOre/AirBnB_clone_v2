#!/usr/bin/python3
"""
Module for Place ORM/FileStorage Class for AirBnB clone - MySQL
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """This class defines Place instance/record attributes"""
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey("cities.id"), nullable=False,)
    user_id = Column(String(60),
                     ForeignKey("users.id"), nullable=False,)
    name = Column(String(128), nullable=False,)
    description = Column(String(1024), default="", nullable=True,)
    number_bathrooms = Column(Integer, default=0, nullable=False,)
    max_guest = Column(Integer, default=0, nullable=False,)
    price_by_night = Column(Integer, default=0, nullable=False,)
    latitude = Column(Float, default=0, nullable=False,)
    longitude = Column(Float, default=0, nullable=False,)
