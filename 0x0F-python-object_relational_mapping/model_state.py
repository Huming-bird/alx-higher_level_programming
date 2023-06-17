#!/usr/bin/python3

''' this script uses SQLAlchemy ORM to cretae table like classes '''

import MySQLdb
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    ''' this class defines all state objects '''

    __tablename__ = 'states'

    id = Column(Integer, Unique=True, autoincrement=True, nullable=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
