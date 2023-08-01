#!/usr/bin/python3
"""
The class is a representation of the state te HBNB application
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class represents a state in the HBNB application.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete-orphan')

    else:
        @property

        def cities(self):
            """
            Getter attribute to return the list of City instances
            with state_id equals to the current State.id.
            """

            from models import storage

            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list if city_list else None
