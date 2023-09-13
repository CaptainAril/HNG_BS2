from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import models

Base = declarative_base()

class Person(Base):
    """Defines Person model class"""
    __tablename__ = 'persons'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    
    def to_dict(self):
        """Serializes Person instance"""
        __dict = self.__dict__.copy()

        del(__dict['_sa_instance_state'])
        return __dict

    def create(self):
        """Creates a new Person instance"""
        models.storage.new(self)
        models.storage.save()

    def update(self, *args, **kwargs):
        """Updates Person instance attribute"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        models.storage.new(self)
        models.storage.save()
    
    def delete(self):
        """Deletes instance for database"""
        models.storage.delete(self)
        models.storage.save()
        