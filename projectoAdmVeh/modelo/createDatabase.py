import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#from DB_vehiculo import makeTable as makeTableVehiculo

def makeEngine(name = "administradorVehiculos.db"):
    engine = create_engine('sqlite:///' + name, echo = True)
    return engine


def makeBase():
    Base = declarative_base()
    return Base

def makeDatabase(engine, base):

    #Base = declarative_base()
    base.metadata.create_all(bind =engine)


