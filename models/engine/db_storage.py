#!/usr/bin/python3
""" New engine """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ DBs class """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, db),
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on current DB session """
        cls_list = [State, City, User, Place, Review, Amenity]
        cls_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                cls_dict[key] = obj
            return cls_dict
        else:
            for cls_name in cls_list:
                for obj in self.__session.query(cls_name):
                    key = obj.__class__.__name__ + '.' + obj.id
                    cls_dict[key] = obj
            return cls_dict

    def new(self, obj):
        """ Add the obj to the current DB """
        self.__session.add(obj)

    def save(self):
        """ commit all changes to the current DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current DB if not none """
        if obj:
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """ create all table in the DB """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        ))
        self.__session = Session()

    def close(self):
        self.__session.close()
