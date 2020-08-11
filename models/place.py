#!/usr/bin/python3
"""
Module for Place ORM/FileStorage Class for AirBnB clone - MySQL
"""
from os import getenv
from models import storage
from sqlalchemy.orm import relationship
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
    description = Column(String(1024), nullable=True,)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False,)
    max_guest = Column(Integer, default=0, nullable=False,)
    price_by_night = Column(Integer, default=0, nullable=False,)
    latitude = Column(Float, nullable=True,)
    longitude = Column(Float, nullable=True,)

    reviews = relationship('Review', backref='place', cascade='all, delete')

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        """ DBStorage """
        @property
        def reviews(self):
            """ Getter, return the list of Review
                instances base in reference place_id => Place.id """
            review_list = []
            for obj in storage.all(Review).values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list
