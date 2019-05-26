import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'price': self.price
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
