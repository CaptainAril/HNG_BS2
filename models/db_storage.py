"""Database Storage module"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.models import Base, Person


class DBStorage:
    """Interacts with mysql database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_DB = getenv('MYSQL_DB')
        MYSQL_HOST = getenv('MYSQL_HOST')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".format(
                        MYSQL_USER,
                        MYSQL_PWD,
                        MYSQL_HOST,
                        MYSQL_DB
                    ))
        
    def reload(self):
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def new(self, obj):
        """Adds new entry to session."""
        self.__session.add(obj)

    def save(self):
        """Saves/commits session changes to database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes entry from database"""
        if obj:
            self.__session.delete(obj)

    def get(self, *args, **kwargs):
        """Retrieves object from database"""
        key, value = list(kwargs.items())[0]
        obj = self.__session.query(
            Person).filter(getattr(Person, key) == value).first()
        return obj
    
    def close(self):
        """Removes current session connection to database"""
        self.__session.remove()