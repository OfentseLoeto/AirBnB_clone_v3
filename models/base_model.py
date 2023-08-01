#!/usr/bin/python3

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime


Base = declarative_base()

class BaseModel:

    id = Column(String(60), primary_key=True, 
            nullable=False, unique=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        if 'password' in dictionary:
            del dictionary['password']
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

