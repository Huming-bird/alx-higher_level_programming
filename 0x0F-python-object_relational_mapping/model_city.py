#!/usr/bin/python3
""" This module is to create a city model """

from sqlalchemy import Column, Integer, String, ForeignKey
import MySQLdb
from model_state import State, Base


class City(Base):
    """thisi is a city class"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
