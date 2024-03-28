#!/usr/bin/python3
'''Contains class definition a State and an instance
Base = desclarative_base'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class
Base = declarative_base()


class State(Base):
    '''Class State'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
