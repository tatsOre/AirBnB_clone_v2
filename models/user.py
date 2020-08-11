#!/usr/bin/python3
"""
Module for User ORM/FileStorage Class for AirBnB clone - MySQL
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Defines all instance attributes for a User instance/record"""
    __tablename__ = 'users'
    email = Column(
        String(128),
        nullable=False,
    )
    password = Column(
        String(128),
        nullable=False,
    )
    first_name = Column(
        String(128),
        nullable=False,
    )
    last_name = Column(
        String(128),
        nullable=False
    )
    places = relationship('Place', backref='user', cascade='all, delete')
