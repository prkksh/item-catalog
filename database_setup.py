import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    """
    Create a Table for storing User Info
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Restaurant(Base):
    """
    Create a Table for storing Restaurant Catalog
    """
    __tablename__ = 'restaurant'

    menu_item = relationship("MenuItem", cascade="all, delete-orphan")
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id
        }


class MenuItem(Base):
    """
    Create a Table for storing Menu Items
    """
    __tablename__ = 'menu_item'

    restaurant = relationship('Restaurant',
                              backref=backref('menu_item',
                                              cascade='all, delete-orphan'))
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
