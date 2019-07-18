import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class _UbicacionVehiculo(Base):


    __tablename__ = "UbicacionVehiculo"

    id = Column(Integer, primary_key = True)
    idvehiculo = Column(Integer, nullable=False, unique=True)
    latitud = Column(String)#foreing key
    longitud = Column(String)#foreing key


def makeTable(eng):

    Base.metadata.create_all(bind =eng)
