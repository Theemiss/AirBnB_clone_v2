#!/usr/bin/python3
"""
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv



class DBStorage:
    """
    """
    __engine = None
    __session = None
    def __init__(self):
        """

        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST =  getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        exec_db = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,HBNB_MYSQL_DB)
        self.__engine = create_engine(exec_db)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        """
        classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
        dicct = {}
        for x in classes:
            if cls is None or cls is classes[x] or cls is x:
                item = self.__session.query(classes[x]).all()
                for y in item:
                    key = y.__class__.__name__ + '.' + y.id
                    dicct[key] = y
        return (dicct)

            

    def new(self,obj):
        """
        """
        self.__session.add(obj)

    def save(self):
        """
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine,expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """
        """
        self.__session.remove()

