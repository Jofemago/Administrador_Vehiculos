import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class _Combustible(Base):

    __tablename__ = "Combustible"

    id = Column(Integer, primary_key = True)
    nombre =  Column(String(15))
    medida =  Column(String(15))


def makeTable(eng):

    Base.metadata.create_all(bind =eng)
