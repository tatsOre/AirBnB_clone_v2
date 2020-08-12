#!/usr/bin/python3
"""
Module for Place ORM/FileStorage Class for AirBnB clone - MySQL
"""
import models
from os import getenv
from models.review import Review
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table


metadata = Base.metadata

place_amenity = Table(
    'place_amenity', metadata,
    Column(
        'place_id', String(60),
        ForeignKey('places.id'),
        primary_key=True, nullable=False,
    ),
    Column(
        'amenity_id', String(60),
        ForeignKey('amenities.id'),
        primary_key=True, nullable=False,
    )
)


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
    amenity_ids = []

    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship(
        'Amenity', secondary=place_amenity,
        viewonly=False, back_populates='place_amenities'
    )

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        """ DBStorage """
        @property
        def reviews(self):
            """ Getter, return the list of Review
                instances base in reference place_id => Place.id """
            review_list = []
            for obj in models.storage.all(Review).values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """Returns list of Amenity instances
                based on amenity_ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute """
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
            else:
                return
