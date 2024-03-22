#!/usr/bin/python3

""" State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class
    Creates a relationship between State (parent) and City (child) classes.
    """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """getter attribute that returns the list of City instances
            if City.state_id==current State_id
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
