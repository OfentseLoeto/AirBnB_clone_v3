#!/usr/bin/python3
"""
The class is a representation of the state te HBNB application
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import storage

class State(BaseModel, Base):
    """
    State class represents a state in the HBNB application.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')

    else:
        @property

        def cities(self):
            """
            Getter attribute to return the list of City instances
            with state_id equals to the current State.id.
            """

            city_list = []
            for city_id, city in models.storage.all('City').items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
